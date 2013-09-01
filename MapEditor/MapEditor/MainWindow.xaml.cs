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

		public MainWindow()
		{
			MainWindow.Instance = this; // >:[

			InitializeComponent();

			this.Loaded += (sender, e) => { this.Initialize(); };
		}

		public Dictionary<string, TileTemplate[]> Templates { get; private set; }

		private void Initialize()
		{
			this.Templates = ManifestReader.Initialize();

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
