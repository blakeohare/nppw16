using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Media.Imaging;

namespace MapEditor
{
	public class TileTemplate
	{
		public int[] ImagePixels { get; set; }
		public string ID { get; set; }
		public string Palette { get; set; }
		public ImageSource ImageSource { get; set; }
	}
}
