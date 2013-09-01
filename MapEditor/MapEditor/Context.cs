using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MapEditor
{
	// Magic Potato
	public static class Context
	{
		private static string svnRoot = null;
		public static string SvnRoot
		{
			get
			{
				if (svnRoot == null)
				{
					string currentDirectory = System.IO.Path.GetFullPath(System.Environment.CurrentDirectory);
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
				}
				return svnRoot;
			}
		}
	}
}
