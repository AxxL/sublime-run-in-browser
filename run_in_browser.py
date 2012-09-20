import sublime, sublime_plugin
# import webbrowser
# import os
import subprocess

class RunInBrowserCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		url = self.view.file_name()
		print "[i] filename: " + url
		url = url.replace('\\', '/')
		# replace path
		url = url.replace('C:/inetpub/wwwroot', 'http://localhost')
		print "[i] url: " + url
		# firefox = webbrowser.get('mozilla')
		# firefox.open_new(url)
		# webbrowser.open_new(url)
		# subprocess.call([r"C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", url])
		#os.system("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", url)
		# os.spawnl(os.P_NOWAIT, "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", r'FireFox', '-new-tab', url)
		pid = subprocess.Popen(["C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", url]).pid
