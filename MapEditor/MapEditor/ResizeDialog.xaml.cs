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
	/// Interaction logic for ResizeDialog.xaml
	/// </summary>
	public partial class ResizeDialog : Window
	{
		private Model model;

		public ResizeDialog(Model model)
		{
			this.model = model;
			InitializeComponent();
			int width = model.Width;
			int height = model.Height;
			this.originalSizeLabel.Text = "Original Size: " + width + " by " + height;
			this.newWidth.Text = width + "";
			this.newHeight.Text = height + "";

			this.horizontalAnchor.SelectedIndex = 0;
			this.verticalAnchor.SelectedIndex = 0;

			this.okButton.Click += (sender, e) => { this.ChangeSize(); };
			this.cancelButton.Click += (sender, e) => { this.Close(); };
		}

		private void ChangeSize()
		{
			int oldWidth = this.model.Width;
			int oldHeight = this.model.Height;
			int newWidth = oldWidth;
			int newHeight = oldHeight;

			if (int.TryParse(this.newWidth.Text, out newWidth) && int.TryParse(this.newHeight.Text, out newHeight))
			{
				if (newWidth > 0 && newHeight > 0)
				{
					if (newWidth != oldWidth || newHeight != oldHeight)
					{
						model.ChangeSize(newWidth, newHeight, this.horizontalAnchor.SelectedIndex == 0, this.verticalAnchor.SelectedIndex == 0);
					}
					this.Close();
					return;
				}
			}

			MessageBox.Show("Invalid Width / Height");
		}
	}
}
