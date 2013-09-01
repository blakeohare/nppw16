using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace MapEditor
{
	/// <summary>
	/// Interaction logic for MainWindow.xaml
	/// </summary>
	public partial class MainWindow : Window
	{
		public static MainWindow Instance { get; private set; }

		private Palette palette;

		public Model ActiveModel { get; set; }

		private TileTemplate[][] drawThis = new TileTemplate[][] { null, null };

		private bool isUpperActive = true;
		private bool isGridOn = false;

		public MainWindow()
		{
			MainWindow.Instance = this; // >:[

			InitializeComponent();

			this.menu_file_exit.Click += (sender, e) => { CommandDoer.Exit(this, this.ActiveModel); };
			this.menu_file_new.Click += (sender, e) => { CommandDoer.New(this, this.ActiveModel); };
			this.menu_file_open.Click += (sender, e) => { CommandDoer.Open(this, this.ActiveModel); };
			this.menu_file_save.Click += (sender, e) => { CommandDoer.Save(this, this.ActiveModel); };
			this.menu_file_saveas.Click += (sender, e) => { CommandDoer.SaveAs(this, this.ActiveModel); };

			this.SizeChanged += (sender, e) =>
			{
				this.artboardBitmap = null;
				this.RedrawTheWholeDamnThing();
			};

			this.layerToggle.Click += (sender, e) => { this.LayerToggle(); };
			this.gridToggle.Click += (sender, e) => { this.GridToggle(); };

			this.clickCatcher.MouseDown += (sender, e) => { this.HandleMouseClick(e.GetPosition(this.clickCatcher), true, e.ChangedButton == MouseButton.Left); };
			this.clickCatcher.MouseUp += (sender, e) => { this.HandleMouseClick(e.GetPosition(this.clickCatcher), false, e.ChangedButton == MouseButton.Left); };
			this.clickCatcher.MouseMove += (sender, e) => { this.HandleMouseMove(e.GetPosition(this.clickCatcher)); };

			this.KeyDown += (sender, e) => { this.HandleKey(e.Key, true); };
			this.KeyUp += (sender, e) => { this.HandleKey(e.Key, false); };

			this.Loaded += (sender, e) => { this.Initialize(); };
			this.LayerToggle();
			this.UpdateTitle();
		}

		private void LayerToggle()
		{
			this.isUpperActive = !this.isUpperActive;
			this.layerToggle.Content = "Current Layer: " + (this.isUpperActive ? "TOP" : "BOTTOM");
		}

		private void GridToggle()
		{
			this.isGridOn = !this.isGridOn;
			this.gridToggle.Content = "Grid: " + (this.isGridOn ? "ON" : "OFF");
			this.RedrawTheWholeDamnThing();
		}

		private bool isMouseDown = false;
		private bool panMode = false;
		private bool isEraseMode = false;

		private int mousePreviousX;
		private int mousePreviousY;
		private int drawBeginPixelX;
		private int drawBeginPixelY;
		private int drawEndPixelX;
		private int drawEndPixelY;

		private void HandleMouseClick(Point p, bool down, bool isPrimary)
		{
			if (this.ActiveModel == null) return;

			this.mousePreviousX = (int)p.X;
			this.mousePreviousY = (int)p.Y;

			if (down)
			{
				if (this.isMouseDown)
				{
					if (this.isEraseMode == isPrimary)
					{
						// revert current region
						this.isMouseDown = false;
						this.clickCatcher.ReleaseMouseCapture();
						this.InvalidateDrawing();
					}
				}
				else
				{
					this.isMouseDown = true;
					this.clickCatcher.CaptureMouse();
					this.panMode = Keyboard.IsKeyDown(Key.Space);
					this.isEraseMode = !isPrimary;
					this.drawBeginPixelX = (int)p.X;
					this.drawBeginPixelY = (int)p.Y;
					this.drawEndPixelX = this.drawBeginPixelX;
					this.drawEndPixelY = this.drawBeginPixelY;
					this.InvalidateDrawing();
				}
			}
			else if (this.isMouseDown)
			{
				this.isMouseDown = false;
				this.clickCatcher.ReleaseMouseCapture();
				if (this.panMode)
				{
				}
				else
				{
					if (isPrimary == !this.isEraseMode)
					{
						this.CommitRectangleRegion(this.isEraseMode);
						this.InvalidateDrawing();
					}
				}
			}
		}

		private void CommitRectangleRegion(bool isEraseMode)
		{
			int left = (this.drawBeginPixelX - this.cameraX) / 16;
			int right = (this.drawEndPixelX - this.cameraX) / 16;
			int top = (this.drawBeginPixelY - this.cameraY) / 16;
			int bottom = (this.drawEndPixelY - this.cameraY) / 16;

			int t;
			if (left > right)
			{
				t = left;
				left = right;
				right = t;
			}

			if (top > bottom)
			{
				t = top;
				top = bottom;
				bottom = t;
			}

			int width = this.ActiveModel.Width;
			int height = this.ActiveModel.Height;

			if (left < 0) left = 0;
			if (top < 0) top = 0;
			if (right >= width) right = width - 1;
			if (bottom >= height) bottom = height - 1;

			bool changed = false;
			TileTemplate[] layer = this.isUpperActive ? this.ActiveModel.TilesUpper : this.ActiveModel.TilesLower;
			for (int y = top; y <= bottom; ++y)
			{
				for (int x = left; x <= right; ++x)
				{
					changed = true;
					layer[y * width + x] = this.isEraseMode ? null : this.ActiveTile;
				}
			}

			if (changed)
			{
				this.ActiveModel.IsDirty = true;
				this.UpdateTitle();
			}
		}

		private void HandleMouseMove(Point p)
		{
			if (this.ActiveModel == null) return;

			int currentX = (int)p.X;
			int currentY = (int)p.Y;

			int col = (currentX - this.cameraX) / 16;
			int row = (currentY - this.cameraY) / 16;

			if (col < 0 || row < 0 || col >= this.ActiveModel.Width || row >= this.ActiveModel.Height)
			{
				this.statusText.Text = "";
			}
			else
			{
				this.statusText.Text = "(" + col + ", " + row + ")";
			}

			if (this.isMouseDown)
			{
				if (this.panMode)
				{
					int dx = currentX - this.mousePreviousX;
					int dy = currentY - this.mousePreviousY;
					this.cameraX += dx;
					this.cameraY += dy;
				}
				else
				{
					this.drawEndPixelX = currentX;
					this.drawEndPixelY = currentY;
				}
				this.mousePreviousX = currentX;
				this.mousePreviousY = currentY;

				this.InvalidateDrawing();
			}
		}

		public void InvalidateDrawing()
		{
			int xStart = (this.drawBeginPixelX - this.cameraX) >> 4;
			int xEnd = (this.drawEndPixelX - this.cameraX) >> 4;
			int yStart = (this.drawBeginPixelY - this.cameraY) >> 4;
			int yEnd = (this.drawEndPixelY - this.cameraY) >> 4;

			int t;

			if (xEnd < xStart)
			{
				t = xEnd;
				xEnd = xStart;
				xStart = t;
			}

			if (yEnd < yStart)
			{
				t = yEnd;
				yEnd = yStart;
				yStart = t;
			}

			int width = this.ActiveModel.Width;
			int height = this.ActiveModel.Height;

			if (xStart < 0) xStart = 0;
			if (yStart < 0) yStart = 0;
			if (xEnd >= width) xEnd = width - 1;
			if (yEnd >= height) yEnd = height - 1;

			if (drawThis[0] == null || drawThis[0].Length != width * height)
			{
				drawThis[0] = new TileTemplate[width * height];
				drawThis[1] = new TileTemplate[width * height];
			}

			for (int i = width * height - 1; i >= 0; --i)
			{
				drawThis[0][i] = this.ActiveModel.TilesLower[i];
				drawThis[1][i] = this.ActiveModel.TilesUpper[i];
			}

			if (this.isMouseDown && !this.panMode)
			{
				TileTemplate[] layer = this.isUpperActive ? drawThis[1] : drawThis[0];
				for (int y = yStart; y <= yEnd; ++y)
				{
					for (int x = xStart; x <= xEnd; ++x)
					{
						layer[y * width + x] = this.isEraseMode ? null : this.ActiveTile;
					}
				}
			}

			this.RedrawTheWholeDamnThing();
		}

		private void HandleKey(Key key, bool down)
		{
			bool shiftPressed = Keyboard.IsKeyDown(Key.LeftShift) || Keyboard.IsKeyDown(Key.RightShift);
			bool ctrlPressed = Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl);

			if (down && !shiftPressed && !ctrlPressed)
			{
				if (key == Key.G)
				{
					this.GridToggle();
				}
				else if (key == Key.L)
				{
					this.LayerToggle();
				}
			}

			if (ctrlPressed)
			{
				switch (key)
				{
					case Key.N:
						CommandDoer.New(this, this.ActiveModel);
						break;

					case Key.O:
						CommandDoer.Open(this, this.ActiveModel);
						break;

					case Key.S:
						if (shiftPressed)
						{
							CommandDoer.SaveAs(this, this.ActiveModel);
						}
						else
						{
							CommandDoer.Save(this, this.ActiveModel);
						}
						break;

					default:
						break;
				}
			}
		}

		private int[] pixels = null;
		private int artboardWidth;
		private int artboardHeight;

		public void RedrawTheWholeDamnThing()
		{
			if (this.artboardBitmap == null)
			{
				int width = (int)(this.clickCatcher.ActualWidth + .5);
				int height = (int)(this.clickCatcher.ActualHeight + .5);

				this.artboardBitmap = new WriteableBitmap(width, height, 96, 96, PixelFormats.Bgra32, null);
				this.pixels = new int[width * height];

				this.artboardWidth = width;
				this.artboardHeight = height;
				this.artboard.Source = this.artboardBitmap;
			}

			// ARGB
			int bgColor = (255 << 24) | (40 << 16) | (40 << 8) | 40;
			for (int i = this.pixels.Length - 1; i >= 0; --i)
			{
				this.pixels[i] = bgColor;
			}

			if (this.ActiveModel != null && this.TileTemplateLookup != null)
			{
				int columns = this.ActiveModel.Width;
				int rows = this.ActiveModel.Height;
				foreach (TileTemplate[] layer in this.drawThis)
				{
					int x = this.cameraX;
					int y = this.cameraY;
					int row, col, px, py, ty;
					int[] imagePixels;
					int targetIndex;
					TileTemplate tile;
					int index = 0;
					int xStart, xEnd, yStart, yEnd;
					for (row = 0; row < rows; ++row)
					{
						x = this.cameraX;
						for (col = 0; col < columns; ++col)
						{
							tile = layer[index++];
							if (tile != null)
							{
								this.blit(tile.ImagePixels, this.pixels, x, y, this.artboardWidth, 16);
							}
							x += 16;
						}
						y += 16;
					}
				}

				if (this.isGridOn)
				{
					int width = columns * 16;
					int height = rows * 16;
					for (int x = 0; x <= columns; ++x)
					{
						this.drawLine(this.pixels, this.artboardWidth, this.cameraX + x * 16, this.cameraY, this.cameraX + x * 16, this.cameraY + rows * 16);
					}

					for (int y = 0; y <= rows; ++y)
					{
						this.drawLine(this.pixels, this.artboardWidth, this.cameraX, this.cameraY + y * 16, this.cameraX + columns * 16, this.cameraY + y * 16);
					}
				}
			}

			this.artboardBitmap.Lock();
			this.artboardBitmap.WritePixels(new Int32Rect(0, 0, this.artboardWidth, this.artboardHeight), this.pixels, this.artboardWidth * 4, 0);
			this.artboardBitmap.Unlock();
		}

		// horizontal or vertical is assumed. No arbitrary angles
		private void drawLine(int[] targetPixels, int pixelWidth, int startX, int startY, int endX, int endY)
		{
			int x, y;
			int width = pixelWidth;
			int height = targetPixels.Length / pixelWidth;

			if (startX > endX)
			{
				x = startX;
				startX = endX;
				endX = x;
			}
			if (startY > endY)
			{
				y = startY;
				startY = endY;
				endY = y;
			}
			int index;
			if (endX == startX)
			{
				x = endX;
				if (x < 0 || x >= width) return;
				if (startY < 0) startY = 0;
				if (endY >= height) endY = height - 1;
				index = startY * width + x;
				for (y = startY; y <= endY; ++y)
				{
					targetPixels[index] = 255 << 24; // black
					index += width;
				}
			}
			else
			{
				y = endY;
				if (y < 0 || y >= height) return;
				if (startX < 0) startX = 0;
				if (endX >= width) endX = width - 1;
				index = y * width + startX;
				for (x = startX; x <= endX; ++x)
				{
					targetPixels[index++] = 255 << 24; //black
				}
			}
		}

		private void blit(int[] sourcePixels, int[] targetPixels, int x, int y, int targetWidth, int sourceWidth)
		{
			int targetHeight = targetPixels.Length / targetWidth;
			int sourceHeight = sourcePixels.Length / sourceWidth;

			int blitWidth = sourceWidth;
			int blitHeight = sourceHeight;

			int startX = 0;
			int startY = 0;

			if (x < 0)
			{
				blitWidth += x;
				startX = -x;
				x = 0;
				if (blitWidth <= 0) return;
			}

			if (y < 0)
			{
				blitHeight += y;
				startY = -y;
				y = 0;
				if (blitHeight <= 0) return;
			}

			if (x + sourceWidth >= targetWidth)
			{
				blitWidth -= (x + sourceWidth - targetWidth) + 1;
				if (blitWidth <= 0) return;
			}

			if (y + sourceHeight >= targetHeight)
			{
				blitHeight -= (y + sourceHeight - targetHeight) + 1;
				if (blitHeight <= 0) return;
			}

			int sourceStartX = startX;
			int sourceEndX = startX + blitWidth - 1;
			int sourceStartY = startY;
			int sourceEndY = startY + blitHeight - 1;
			int targetIndex, sourceIndex;
			int sourceX, sourceY;
			int color;

			for (sourceY = sourceStartY; sourceY <= sourceEndY; ++sourceY)
			{
				sourceIndex = sourceY * sourceWidth + sourceStartX;
				targetIndex = y * targetWidth + x;
				for (sourceX = sourceStartX; sourceX <= sourceEndX; ++sourceX)
				{
					color = sourcePixels[sourceIndex++];
					if (((color >> 24) & 255) == 0)
					{
						++targetIndex;
					}
					else
					{
						targetPixels[targetIndex++] = color;
					}
				}
				++y;
			}
		}

		private int cameraX = 0;
		private int cameraY = 0;

		public Dictionary<string, TileTemplate[]> Templates { get; private set; }
		public Dictionary<string, TileTemplate> TileTemplateLookup { get; private set; }

		private void Initialize()
		{
			this.Templates = ManifestReader.Initialize();

			Dictionary<string, TileTemplate> lookup = new Dictionary<string, TileTemplate>();
			foreach (TileTemplate[] templates in this.Templates.Values)
			{
				foreach (TileTemplate template in templates)
				{
					lookup[template.ID] = template;
				}
			}
			this.TileTemplateLookup = lookup;

			this.palette = new Palette(this.Templates.Keys.ToArray());
			this.paletteHost.Children.Add(this.palette);

			this.GridToggle();
		}

		public TileTemplate ActiveTile { get; set; }

		public void SetActiveTile(TileTemplate template)
		{
			this.ActiveTile = template;
		}

		private System.Windows.Media.Imaging.WriteableBitmap artboardBitmap;

		public void UpdateTitle()
		{
			this.Title = this.ActiveModel == null ? "Space Squirrel Map Editor" : "Space Squirrel Map Editor: " + this.ActiveModel.DisplayName;
		}
	}
}
