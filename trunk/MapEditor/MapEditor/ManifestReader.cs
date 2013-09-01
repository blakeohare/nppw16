using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MapEditor
{
	public class ManifestReader
	{
		public static Dictionary<string, TileTemplate[]> Initialize()
		{
			string tileDirectory = FindTileDirectory();
			List<TileTemplate> tileTemplates = new List<TileTemplate>();

			string[] manifest = System.IO.File.ReadAllText(System.IO.Path.Combine(tileDirectory, "manifest.txt")).Split('\n');
			int i = 0;
			foreach (string line in manifest)
			{
				++i;
				string trimmed = line.Split('#')[0].Trim();
				if (trimmed.Length > 0)
				{
					string[] parts = trimmed.Split('\t');
					if (parts.Length != 3)
					{
						throw new Exception("Tile manifest error. Talk to Spears or Blake. Line: " + line);
					}

					string id = parts[0];
					string imagePath = parts[2].Split(',')[0].Trim();

					System.Windows.Media.Imaging.BitmapImage bmp = ImageLoader.LoadImage(System.IO.Path.Combine(tileDirectory, imagePath.Replace('/', System.IO.Path.DirectorySeparatorChar)));
					int[] pixels = ImageLoader.GetPixels(bmp);
					tileTemplates.Add(new TileTemplate() { ID = id, ImagePixels = pixels, Palette = System.IO.Path.GetDirectoryName(imagePath), ImageSource = bmp });
				}
			}

			Dictionary<string, List<TileTemplate>> templatesByPalette = new Dictionary<string, List<TileTemplate>>();

			foreach (TileTemplate template in tileTemplates)
			{
				List<TileTemplate> templates;
				if (!templatesByPalette.TryGetValue(template.Palette, out templates))
				{
					templates = new List<TileTemplate>();
					templatesByPalette[template.Palette] = templates;
				}
				templates.Add(template);
			}

			Dictionary<string, TileTemplate[]> output = new Dictionary<string, TileTemplate[]>();
			foreach (string key in templatesByPalette.Keys)
			{
				output[key] = templatesByPalette[key].ToArray();
			}

			return output;
		}

		// This is a horrible horrible hack and that's okay.
		private static string FindTileDirectory()
		{
			return System.IO.Path.Combine(Context.SvnRoot, "images", "tiles");
		}
	}
}
