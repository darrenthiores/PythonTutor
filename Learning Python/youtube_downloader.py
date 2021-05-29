# Youtube video downloader project

from pytube import YouTube

# link
link = input('Youtube Link : ')
yt = YouTube(link)

# Youtube's video informations
youtube_title = yt.title
youtube_views = yt.views
youtube_length = yt.length
youtube_rating = yt.rating
print (f'Title : {youtube_title}')
print (f'Number of views : {youtube_views}')
print (f'Length of video : {youtube_length}')
print (f'Rating of videos : {youtube_rating}')

# To get the highest resolution possible
ys = yt.streams.get_highest_resolution()

# Download started
print ('Downloading...')
ys.download()
print ('Download completed!!')