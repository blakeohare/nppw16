using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MapEditor
{
	public class Model
	{
		public bool IsDirty { get; set; }

		public string Path { get; set; }

		public int Width { get; set; }
		public int Height { get; set; }

		public bool IsSideScroll { get; set; }

		// High frequency access, field that behaves like a property for performance.
		public TileTemplate[] TilesUpper;
		public TileTemplate[] TilesLower;


		public Model(int width, int height)
		{
			this.Path = null;
			this.Width = width;
			this.Height = height;
			this.IsDirty = true;
			this.TilesLower = new TileTemplate[width * height];
			this.TilesUpper = new TileTemplate[width * height];
			this.values = new Dictionary<string, string>();
			this.IsSideScroll = true;
		}

		public string DisplayName
		{
			get
			{
				return
					(this.Path == null
						? "Untitled.map"
						: System.IO.Path.GetFileName(this.Path)) +
					(this.IsDirty
						? "*"
						: "");

			}
		}

		public string Serialize()
		{
			this.values["width"] = "" + this.Width;
			this.values["height"] = "" + this.Height;
			this.values["upper"] = this.SerializeTiles(this.TilesUpper);
			this.values["lower"] = this.SerializeTiles(this.TilesLower);
			this.values["view"] = this.IsSideScroll ? "side" : "over";

			List<string> output = new List<string>();
			foreach (string key in this.values.Keys)
			{
				output.Add("#" + key + ":" + this.values[key]);
			}

			return string.Join("\n", output);
		}

		private string SerializeTiles(IList<TileTemplate> tiles)
		{
			return string.Join(",", tiles.Select<TileTemplate, string>(tile => tile == null ? "" : tile.ID));
		}

		public void SetTiles(TileTemplate[] tiles, bool upperLayer)
		{
			if (upperLayer)
			{
				this.TilesUpper = tiles;
			}
			else
			{
				this.TilesLower = tiles;
			}
		}

		private Dictionary<string, string> values;
		public void SetRawFileData(Dictionary<string, string> values)
		{
			this.values = values;
		}

		public void ChangeSize(int newWidth, int newHeight, bool anchorLeft, bool anchorTop)
		{
			TileTemplate[] newUpperTiles = new TileTemplate[newWidth * newHeight];
			TileTemplate[] newLowerTiles = new TileTemplate[newWidth * newHeight];

			TileTemplate[] source, target;
			int oldWidth = this.Width;
			int oldHeight = this.Height;

			foreach (bool isUpper in new bool[] { true, false })
			{
				source = isUpper ? this.TilesUpper : this.TilesLower;
				target = isUpper ? newUpperTiles : newLowerTiles;
				int offsetX = anchorLeft ? 0 : newWidth - this.Width;
				int offsetY = anchorTop ? 0 : newHeight - this.Height;
				int tx, ty;
				for (int y = 0; y < this.Height; ++y)
				{
					ty = y + offsetY;
					for (int x = 0; x < this.Width; ++x)
					{
						tx = x + offsetX;
						if (tx < 0 || tx >= newWidth || ty < 0 || ty >= newHeight)
						{
						}
						else
						{
							target[ty * newWidth + tx] = source[y * oldWidth + x];
						}
					}
				}
			}

			this.Width = newWidth;
			this.Height = newHeight;

			this.TilesLower = newLowerTiles;
			this.TilesUpper = newUpperTiles;

			this.IsDirty = true;
			MainWindow.Instance.UpdateTitle();
			MainWindow.Instance.InvalidateDrawing();
		}
	}
}
