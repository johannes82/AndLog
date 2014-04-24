import sublime, sublime_plugin

def plugin_loaded():
	print ('AndLog plugin loaded.')
	global Pref

	settings = sublime.load_settings('AndLog.sublime-settings')


	class Pref:
		def load(self):
			Pref.highlighting_mode = settings.get('highlighting_mode', "verbose")
			Pref.enabled           = True


	Pref = Pref()
	Pref.load()


class EnableHighlightingCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		# Pref.enabled = not Pref.enabled
		print ('AndLog enabled:', Pref.enabled)
		print ('AndLog mode:', Pref.highlighting_mode)
		if (Pref.enabled):
			HighlightTextCommand()


class HighlightTextCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		region = view.find_all("Exception", True)
		view.add_regions("AndLog", region, "Exception", "", True)


class ClearHighlightCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		view.erase_regions("AndLog")
