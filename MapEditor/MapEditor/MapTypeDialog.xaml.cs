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
using System.Windows.Shapes;

namespace MapEditor
{
	/// <summary>
	/// Interaction logic for MapTypeDialog.xaml
	/// </summary>
	public partial class MapTypeDialog : Window
	{
		public MapTypeDialog(Model model)
		{
			InitializeComponent();
			this.picker.SelectedIndex = model.IsSideScroll ? 0 : 1;

			this.okButton.Click += (sender, e) =>
			{
				bool isSidescroll = this.picker.SelectedIndex == 0;
				if (model.IsSideScroll != isSidescroll)
				{
					model.IsSideScroll = isSidescroll;
					model.IsDirty = true;
					MainWindow.Instance.UpdateTitle();
				}
				this.Close();
			};

			this.cancelButton.Click += (sender, e) =>
			{
				this.DialogResult = false;
				this.Close();
			};
		}
	}
}
