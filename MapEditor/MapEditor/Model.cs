using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MapEditor
{
	public class Model
	{
		public bool IsDirty { get; set; }

		public string Path { get; set; }

		public int Width { get; set; }
		public int Height { get; set; }

		// High frequency access, field that behaves like a property for performance.
		public TileTemplate[] TilesUpper;
		public TileTemplate[] TilesLower;


		public Model(int width, int height)
		{
			this.Path = null;
			this.Width = width;
			this.Height = height;
			this.IsDirty = true;
			this.TilesLower = new TileTemplate[width * height];
			this.TilesUpper = new TileTemplate[width * height];
			this.values = new Dictionary<string, string>();
		}

		public string DisplayName
		{
			get
			{
				return
					(this.Path == null
						? "Untitled.map"
						: System.IO.Path.GetFileName(this.Path)) +
					(this.IsDirty
						? "*"
						: "");

			}
		}

		public string Serialize()
		{
			this.values["width"] = "" + this.Width;
			this.values["height"] = "" + this.Height;
			this.values["upper"] = this.SerializeTiles(this.TilesUpper);
			this.values["lower"] = this.SerializeTiles(this.TilesLower);

			List<string> output = new List<string>();
			foreach (string key in this.values.Keys)
			{
				output.Add("#" + key + ":" + this.values[key]);
			}

			return string.Join("\n", output);
		}

		private string SerializeTiles(IList<TileTemplate> tiles)
		{
			return string.Join(",", tiles.Select<TileTemplate, string>(tile => tile == null ? "" : tile.ID));
		}

		public void SetTiles(TileTemplate[] tiles, bool upperLayer)
		{
			if (upperLayer)
			{
				this.TilesUpper = tiles;
			}
			else
			{
				this.TilesLower = tiles;
			}
		}

		private Dictionary<string, string> values;
		public void SetRawFileData(Dictionary<string, string> values)
		{
			this.values = values;
		}
	}
}
