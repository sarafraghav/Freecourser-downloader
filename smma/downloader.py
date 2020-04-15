from zippyshare_generator import zippyshare
generator = zippyshare()
url_download = generator.generate("https://www110.zippyshare.com/v/0CtTucxG/file.html")
generator.download(url_download, ".", "myMovies.mp4", False)
#it will download it automaticall