import sublime
import sublime_plugin
import re
import subprocess

class GoToRedmineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		BASE_URL = "FILL_HERE"
		selection = self.view.sel()
		selectedTexts = [self.view.substr(self.view.word(region)) for region in selection]
		redmineIds = { text for text in selectedTexts if re.match(r"^\d+$", text) }
		for text in redmineIds:
			url = BASE_URL + "/issues/{}".format(text)
			subprocess.Popen("start {}".format(url), shell=True)