import re
import sublime, sublime_plugin

__author__ = 'johannes82'

# global pattern
# pattern = r'(([0-1][0-9]-[0-3][\d]\s[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\.\d\d\d)(\s*|:)(\d*:\s*\d*\s)(V|I|W|D|E)/($|[^\[$\n]*))'

global info_pattern
info_pattern = r'([0-1][0-9]-[0-3][\d]\s[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\.\d\d\d(\s*|:)\d*:\s*\d*\s(I)/($|[^\[$\n]*))'
global verbose_pattern
verbose_pattern = r'([0-1][0-9]-[0-3][\d]\s[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\.\d\d\d(\s*|:)\d*:\s*\d*\s(V)/($|[^\[$\n]*))'
global warning_pattern
warning_pattern = r'([0-1][0-9]-[0-3][\d]\s[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\.\d\d\d(\s*|:)\d*:\s*\d*\s(W)/($|[^\[$\n]*))'
global debug_pattern
debug_pattern = r'([0-1][0-9]-[0-3][\d]\s[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\.\d\d\d(\s*|:)\d*:\s*\d*\s(D)/($|[^\[$\n]*))'
global error_pattern
error_pattern = r'([0-1][0-9]-[0-3][\d]\s[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\.\d\d\d(\s*|:)\d*:\s*\d*\s(E)/($|[^\[$\n]*))'


def plugin_loaded():
	print ('AndLog plugin loaded.')
	global Pref
	Pref = Pref()
	Pref.load()


class Pref:
	def load(self):
		settings = sublime.load_settings('AndLog.sublime-settings')
		Pref.highlighting_mode   = settings.get('highlighting_mode', "verbose")
		Pref.highlighted         = False
		Pref.color_scope_info    = settings.get('color_scope_info', "comment")
		Pref.color_scope_verbose = settings.get('color_scope_verbose', "support.type.exception")
		Pref.color_scope_warning = settings.get('color_scope_warning', "comment")
		Pref.color_scope_debug   = settings.get('color_scope_debug', "string")
		Pref.color_scope_error   = settings.get('color_scope_error', "invalid")


class EnableHighlightingCommand(sublime_plugin.TextCommand):
	"""
	Command for highlighting static logfiles.
	"""
	def run(self, edit):
		global Pref

		if not (Pref.highlighted):
			Pref.highlighted = True
			print ("Highlighting", Pref.highlighted)
			# self.highlight_text(self.view, info_pattern, Pref.color_scope_info)
			self.highlight_text(self.view, verbose_pattern, Pref.color_scope_verbose)
			self.highlight_text(self.view, warning_pattern, Pref.color_scope_warning)
			self.highlight_text(self.view, debug_pattern, Pref.color_scope_debug)
			self.highlight_text(self.view, error_pattern, Pref.color_scope_error)
		else:
			Pref.highlighted = False
			print ("Highlighting", Pref.highlighted)
			self.view.erase_regions("AndLog" + info_pattern)
			self.view.erase_regions("AndLog" + verbose_pattern)
			self.view.erase_regions("AndLog" + warning_pattern)
			self.view.erase_regions("AndLog" + debug_pattern)
			self.view.erase_regions("AndLog" + error_pattern)


	def highlight_text(self, view, pattern, color):
		print ("Highlighting ", pattern, "with color", color)
		regions = []
		regions += view.find_all(pattern, False)
		key = "AndLog" + pattern
		view.add_regions(key, regions, color, "", True)


class StartLiveLoggingCommand(sublime_plugin.TextCommand):
	"""
	Command for live logging endless.
	"""
	def run(self, edit):
		print ("This is not implemented yet.")
