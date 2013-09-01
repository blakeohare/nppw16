using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MapEditor
{
	public class MapParser
	{
		private string filename;
		Dictionary<string, TileTemplate> tileLookup;
		public MapParser(string filename, Dictionary<string, TileTemplate> tileLookup)
		{
			this.filename = filename;
			this.tileLookup = tileLookup;
		}

		public Model Parse()
		{
			Dictionary<string, string> values = new Dictionary<string, string>();
			string[] lines = System.IO.File.ReadAllText(this.filename).Replace("\r\n", "\n").Replace('\r', '\n').Split('\n');
			foreach (string line in lines)
			{
				string[] parts = line.Split(':');
				if (parts.Length >= 2)
				{
					string key = parts[0];
					if (key.Length > 0 && key[0] == '#')
					{
						key = key.Substring(1);
						string value = parts[1];
						for (int i = 2; i < parts.Length; ++i)
						{
							value += ':' + parts[i];
						}

						values[key] = value;
					}
				}
			}

			int width = int.Parse(values["width"]);
			int height = int.Parse(values["height"]); // let it crash if this is wrong.

			Model model = new Model(width, height);

			TileTemplate[] topLayer = new TileTemplate[width * height];
			TileTemplate[] bottomLayer = new TileTemplate[width * height];

			string[] tileIdsUpper = values["upper"].Split(',');
			string[] tileIdsLower = values["lower"].Split(',');

			for (int i = width * height - 1; i >= 0; --i)
			{
				string tileId = tileIdsUpper[i].Trim();
				if (tileId.Length > 0)
				{
					topLayer[i] = this.tileLookup[tileId];
				}

				tileId = tileIdsLower[i].Trim();
				if (tileId.Length > 0)
				{
					bottomLayer[i] = this.tileLookup[tileId];
				}
			}

			// TODO: other fields

			model.SetTiles(topLayer, true);
			model.SetTiles(bottomLayer, false);

			model.SetRawFileData(values);

			model.Path = filename;
			model.IsSideScroll = !values.ContainsKey("view") || values["view"].Trim().ToLowerInvariant() != "over";

			return model;
		}
	}
}
