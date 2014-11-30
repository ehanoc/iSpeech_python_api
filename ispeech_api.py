import urllib
import urllib2

# -------- Init -----------
f = open("ispeech_api_key")
api_key_ispech = f.readline()

output_file = "../audiofile.mp3"

api_data_format = "rest"
url_base_ispeech = "http://api.ispeech.org/api/"+ api_data_format + "?apikey=" + api_key_ispech
# -------------------------

def fetch_url(url):
    response = urllib2.urlopen(url)
    return response.read()

def fetch_audio_for_text(text, voice="ukenglishfemale"):
    text = unicode(text).encode("utf-8")
    text = urllib.quote_plus(text)

    voice = unicode(voice).encode("utf-8")
    voice = urllib.quote_plus(voice)

    urllib.urlretrieve(url_base_ispeech
                       + "&action=convert&text="
                       + text
                       + "&Voice="+voice, output_file)
    return output_file
