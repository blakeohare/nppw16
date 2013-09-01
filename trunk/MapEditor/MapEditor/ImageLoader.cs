using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MapEditor
{
	public static class ImageLoader
	{
		public static System.Windows.Media.Imaging.BitmapImage LoadImage(string path)
		{
			return new System.Windows.Media.Imaging.BitmapImage(new Uri(path, UriKind.Absolute));
		}

		public static int[] GetPixels(System.Windows.Media.Imaging.BitmapImage imageSource)
		{
			System.Windows.Media.Imaging.WriteableBitmap wbmp = new System.Windows.Media.Imaging.WriteableBitmap(imageSource);
			int[] pixels = new int[wbmp.PixelWidth * wbmp.PixelHeight];
			wbmp.CopyPixels(pixels, wbmp.PixelWidth * 4, 0);
			return pixels;
		}
	}
}
