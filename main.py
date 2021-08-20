import sublime
import sublime_plugin
import re
import subprocess

class GoToRedmineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings("Go to redmine.sublime-settings")
		baseUrl = settings.get("base_url")
		if baseUrl is None:
			sublime.error_message("[Error] No value found for base_url. Please go to Preferences > Package Settings > Go to redmine > Settings.")
		else:
			selection = self.view.sel()
			selectedTexts = [self.view.substr(self.view.word(region)) for region in selection]
			redmineIds = { text for text in selectedTexts if re.match(r"^\d+$", text) }
			for text in redmineIds:
				url = baseUrl + "/issues/{}".format(text)
				subprocess.Popen("start {}".format(url), shell=True)