#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# github : https://github.com/muntazir-halim
# ---------------------
import requests,os,random
class ruks:	
	def __init__(self):
		self.R = '\033[1;31m'
		self.G ='\033[1;32m'
		self.w ='\033[1;39m'
		print("""                                                               
  ___                  _              _   _   _ _   _       _    
 |   \ _____ __ ___ _ | |___  __ _ __| | | |_(_) |_| |_ ___| |__ 
 | |) / _ \ V  V / ' \| / _ \/ _` / _` | |  _| | / /  _/ _ \ / / 
 |___/\___/\_/\_/|_||_|_\___/\__,_\__,_|  \__|_|_\_\\__\___/_\_\ 
      
                    - code by ruks -
""")	
		self.url=str(input(f"   {self.G}⌯ {self.w}Enter the video link from Tik Tok :"))
		if "https://" not in self.url:
			exit(0)
		os.system("clear")
		print(f"""
	{self.R}#{self.w}-------------{self.G}download{self.w}-------------{self.R}#{self.w}
	|  [01] Download video no watermark|
	|  [02] Download video watermark   |
	|  [03] Download picture           |
	|  [04] Download music video       |
	{self.R}#{self.w}----------------------------------{self.R}#{self.w}""")
		print()		
		self.en=int(input(f"   {self.G}⌯ {self.w}Enter a suitable number :"))
		self.http = requests.Session()
	def ren(self):
		self.res=self.http.get(f"https://godownloader.com/api/tiktok-no-watermark-free?url={self.url}&key=godownloader.com").json()	
		self.rank()						
	def rank(self):
		if self.en == int("1" or "01"):			
			self.entrance = self.res["video_no_watermark"]
			pass
		elif self.en == int("2" or "03"):
			self.entrance=self.res["video_watermark"]
			pass
		elif self.en == int("3" or "03"):
			self.entrance=self.res["author_cover"]	
			pass
		elif self.en == int("4" or "04"):
			self.entrance=self.res["music_url"]
			pass
		else:
			exit(0)
		self.download()
		
	def download(self):
		self.req = self.http.get(self.entrance).content
		self.ren = str("".join(random.choice("1234567890ruks")for i in range(5)))
		if self.en == int("1" or "01"):
			# Save to video file for mobile : /sdcard/DCIM/
			with open(f"{self.ren}.mp4", 'wb') as f:
				f.write(self.req)
				f.flush()
				print(f"{self.G}⌯ {self.w}It has been downloaded successfully")
			pass
		elif self.en == int("2" or "02"):
			with open(f"{self.ren}.mp4", 'wb') as f:
				f.write(self.req)
				f.flush()
				print(f"{self.G}⌯ {self.w}It has been downloaded successfully")			
			pass
		elif self.en == int("3" or "03"):
			with open(f"{self.ren}.jpg", 'wb') as f:
				f.write(self.req)
				f.flush()
				print(f"{self.G}⌯ {self.w}It has been downloaded successfully")			
			pass
		elif self.en == int("4" or "04"):
			with open(f"{self.ren}.mp3", 'wb') as f:
				f.write(self.req)
				f.flush()
				print(f"{self.G}⌯ {self.w}It has been downloaded successfully")			
			pass
ruks().ren()		
		