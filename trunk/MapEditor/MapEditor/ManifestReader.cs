using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MapEditor
{
	public class ManifestReader
	{

		public static void Initialize()
		{
			string tileDirectory = FindTileDirectory();
			
		}

		// This is a horrible horrible hack and that's okay.
		private static string FindTileDirectory()
		{
			string currentDirectory = System.IO.Path.GetFullPath(System.Environment.CurrentDirectory);
			string svnRoot = null;
			while (svnRoot == null)
			{
				string checkForThis = System.IO.Path.Combine(currentDirectory, "License.txt");
				if (System.IO.File.Exists(checkForThis))
				{
					svnRoot = currentDirectory;
				}
				else
				{
					currentDirectory = System.IO.Path.GetDirectoryName(currentDirectory);
				}
			}

			return System.IO.Path.Combine(svnRoot, "images", "tiles");
		}
	}
}
