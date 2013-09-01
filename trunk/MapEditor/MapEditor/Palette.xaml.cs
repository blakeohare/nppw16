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
	/// Interaction logic for Palette.xaml
	/// </summary>
	public partial class Palette : UserControl
	{
		public Palette(string[] palettes)
		{
			InitializeComponent();

			this.palettesCombobox.ItemsSource = palettes;
			this.palettesCombobox.SelectionChanged += (sender, e) => { this.PickPalette(); };
			this.palettesCombobox.SelectedIndex = 0;
		}

		private void PickPalette()
		{
			string key = this.palettesCombobox.SelectedItem.ToString();
			this.Update(MainWindow.Instance.Templates[key]);
		}

		public void Update(TileTemplate[] activePalette)
		{
			this.listbox.ItemsSource = activePalette;
			this.listbox.SelectionChanged += (sender, e) => { MainWindow.Instance.SetActiveTile(this.listbox.SelectedItem as TileTemplate); };

		}
	}
}
