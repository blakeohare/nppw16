using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MapEditor
{
	public static class CommandDoer
	{
		// returns false if next action should be canceled.
		private static bool PromptSave(MainWindow window, Model model) {
			System.Windows.MessageBoxResult result = System.Windows.MessageBox.Show("Document has unsaved changes. Do you wish to save?");
			if (result == System.Windows.MessageBoxResult.Cancel) return false; // hit Cancel? stop action
			if (result == System.Windows.MessageBoxResult.No) return true; // hit No? continue with action

			return CommandDoer.Save(window, model); // hit yes but then hit cancel? stop action
		}

		public static void Exit(MainWindow window, Model model)
		{
			if (model.IsDirty)
			{
				if (CommandDoer.PromptSave(window, model))
				{
					window.Close();
				}
				else
				{
					// do nothing.
				}
			}	
			else
			{
				window.Close();
			}
		}

		public static void New(MainWindow window, Model model)
		{
			window.ActiveModel = new Model(16, 14);
			window.InvalidateDrawing();
		}

		public static string MapsDirectory
		{
			get { return System.IO.Path.Combine(Context.SvnRoot, "maps"); }
		}

		public static void Open(MainWindow window, Model model)
		{
			bool goAhead = true;
			if (model.IsDirty && !CommandDoer.PromptSave(window, model))
			{
				goAhead = false;
			}

			if (goAhead)
			{
				System.Windows.Forms.OpenFileDialog ofd = new System.Windows.Forms.OpenFileDialog();
				ofd.InitialDirectory = CommandDoer.MapsDirectory;
				System.Windows.Forms.DialogResult result = ofd.ShowDialog();
				if (result == System.Windows.Forms.DialogResult.OK)
				{
					string filename = ofd.FileName;
					MapParser mapParser = new MapParser(filename, window.TileTemplateLookup);
					window.ActiveModel = mapParser.Parse();
					window.RedrawTheWholeDamnThing();
					window.UpdateTitle();
				}
			}
		}

		// returns false if the user hit cancel or the document was not saved.
		public static bool Save(MainWindow window, Model model)
		{
			
			return false;
		}

		public static void SaveAs(MainWindow window, Model model)
		{

		}
	}
}
