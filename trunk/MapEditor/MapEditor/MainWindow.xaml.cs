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

		public Model ActiveModel  { get; set; }

		public MainWindow()
		{
			MainWindow.Instance = this; // >:[

			InitializeComponent();

			this.menu_file_exit.Click += (sender, e) => { CommandDoer.Exit(this, this.ActiveModel); };
			this.menu_file_new.Click += (sender, e) => { CommandDoer.New(this, this.ActiveModel); };
			this.menu_file_open.Click += (sender, e) => { CommandDoer.Open(this, this.ActiveModel); };
			this.menu_file_save.Click += (sender, e) => { CommandDoer.Save(this, this.ActiveModel); };
			this.menu_file_saveas.Click += (sender, e) => { CommandDoer.SaveAs(this, this.ActiveModel); };

			this.Loaded += (sender, e) => { this.Initialize(); };
		}

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

			this.palette = new Palette(this.Templates.Keys.ToArray());
			this.paletteHost.Children.Add(this.palette);
		}

		public TileTemplate ActiveTile { get; set; }

		public void SetActiveTile(TileTemplate template)
		{
			this.ActiveTile = template;
		}
	}
}
