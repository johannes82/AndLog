import re
import sublime, sublime_plugin

__author__ = 'johannes82'

# global pattern
# pattern = r'(([0-1][0-9]-[0-3][\d]\s[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\.\d\d\d)(\s*|:)(\d*:\s*\d*\s)(V|I|W|D|E)/($|[^\[$\n]*))'

base_pattern = '^(\[\s)*[0-1][0-9]-[0-3][\d]\s[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\.\d\d\d(\s*|:)\d*:\s*\d*\s'
global info_pattern
info_pattern = r'(' + base_pattern + '(I)/.*[^\n])'
global verbose_pattern
verbose_pattern = r'(' + base_pattern + '(V)/.*[^\n])'
global warning_pattern
warning_pattern = r'(' + base_pattern + '(W)/.*[^\n])'
global debug_pattern
debug_pattern = r'(' + base_pattern + '(D)/.*[^\n])'
global error_pattern
error_pattern = r'(' + base_pattern + '(E)/.+[^\n])'


def plugin_loaded():
	print ('AndLog plugin loaded.')
	global Pref
	Pref = Pref()
	Pref.load()


	def highlight_text(view, pattern, color):
		"""
		Function for highlighting text in a specific region that is matched by pattern.
		"""
		print ("Highlighting ", pattern, "with color", color)
		regions = []
		regions += view.find_all(pattern, False)
		key = pattern
		view.add_regions(key, regions, color, "", True)


	def clear_highlight(view):
		"""
		Clear all known highlighting.
		"""
		view.erase_regions(info_pattern)
		view.erase_regions(verbose_pattern)
		view.erase_regions(warning_pattern)
		view.erase_regions(debug_pattern)
		view.erase_regions(error_pattern)


class Pref:
	def load(self):
		settings = sublime.load_settings('AndLog.sublime-settings')
		Pref.highlighting_info      = settings.get('highlighting_info', False)
		Pref.highlighting_verbose   = settings.get('highlighting_verbose', False)
		Pref.highlighting_warning   = settings.get('highlighting_warning', False)
		Pref.highlighting_debug     = settings.get('highlighting_debug', True)
		Pref.highlighting_error     = settings.get('highlighting_error', True)
		Pref.highlighted         = False
		Pref.color_scope_info    = settings.get('color_scope_info', "comment")
		Pref.color_scope_verbose = settings.get('color_scope_verbose', "support.type.exception")
		Pref.color_scope_warning = settings.get('color_scope_warning', "comment")
		Pref.color_scope_debug   = settings.get('color_scope_debug', "string")
		Pref.color_scope_error   = settings.get('color_scope_error', "invalid")


class ToggleAllHighlightingCommand(sublime_plugin.TextCommand):
	"""
	Command for highlighting static logfiles.
	"""
	def run(self, edit):
		global Pref

		if not (Pref.highlighted):
			Pref.highlighted = True
			print ("Highlighting", Pref.highlighted)
			if (Pref.highlighting_info):
				highlight_text(self.view, info_pattern, Pref.color_scope_info)
			if (Pref.highlighting_verbose):
				highlight_text(self.view, verbose_pattern, Pref.color_scope_verbose)
			if (Pref.highlighting_warning):
				highlight_text(self.view, warning_pattern, Pref.color_scope_warning)
			if (Pref.highlighting_debug):
				highlight_text(self.view, debug_pattern, Pref.color_scope_debug)
			if (Pref.highlighting_error):
				highlight_text(self.view, error_pattern, Pref.color_scope_error)
		else:
			Pref.highlighted = False
			print ("Highlighting", Pref.highlighted)
			clear_highlight(self.view)


class ToggleInfoHighlightingCommand(sublime_plugin.TextCommand):
	"""
	Command for highlighting static logfiles.
	"""
	def run(self, edit):
		global Pref

		if not (Pref.highlighted):
			Pref.highlighted = True
			highlight_text(self.view, info_pattern, Pref.color_scope_info)
		else:
			Pref.highlighted = False
			clear_highlight(self.view)


class ToggleVerboseHighlightingCommand(sublime_plugin.TextCommand):
	"""
	Command for highlighting static logfiles.
	"""
	def run(self, edit):
		global Pref

		if not (Pref.highlighted):
			Pref.highlighted = True
			highlight_text(self.view, verbose_pattern, Pref.color_scope_verbose)
		else:
			Pref.highlighted = False
			clear_highlight(self.view)


class ToggleWarningHighlightingCommand(sublime_plugin.TextCommand):
	"""
	Command for highlighting static logfiles.
	"""
	def run(self, edit):
		global Pref

		if not (Pref.highlighted):
			Pref.highlighted = True
			highlight_text(self.view, warning_pattern, Pref.color_scope_warning)
		else:
			Pref.highlighted = False
			clear_highlight(self.view)


class ToggleDebugHighlightingCommand(sublime_plugin.TextCommand):
	"""
	Command for highlighting static logfiles.
	"""
	def run(self, edit):
		global Pref

		if not (Pref.highlighted):
			Pref.highlighted = True
			highlight_text(self.view, debug_pattern, Pref.color_scope_debug)
		else:
			Pref.highlighted = False
			clear_highlight(self.view)


class ToggleErrorHighlightingCommand(sublime_plugin.TextCommand):
	"""
	Command for highlighting static logfiles.
	"""
	def run(self, edit):
		global Pref

		if not (Pref.highlighted):
			Pref.highlighted = True
			highlight_text(self.view, error_pattern, Pref.color_scope_error)
		else:
			Pref.highlighted = False
			clear_highlight(self.view)


class ToggleCustomHighlightingCommand(sublime_plugin.WindowCommand):
	"""
	Command for highlighting custom tags.
	"""
	def run(self):
		global Pref
		caption = "Type a tag to filter for"
		initial_text = ""

		self.window.show_input_panel(caption, initial_text, self.highlight, None, None)


	def highlight(self, user_input):
		self.custom_pattern = r'(' + base_pattern + '([IVWDE])/' + user_input + '.+[^\n])'
		if not (Pref.highlighted):
			Pref.highlighted = True
			highlight_text(self.window.active_view(), self.custom_pattern, Pref.color_scope_error)
		else:
			Pref.highlighted = False
			self.window.active_view().erase_regions(self.custom_pattern)


class StartLiveLoggingCommand(sublime_plugin.TextCommand):
	"""
	Command for live logging endless.
	"""
	def run(self, edit):
		print ("This is not implemented yet.")

