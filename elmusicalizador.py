import winsound as ws
import pygame.mixer
import random as r_int

cache = list()
random = r_int.randint(0, 32000)
mus = list()

def cacheapp(mus):
	cache.append(mus)
	if len(cache) > 10:
		cache.pop(-1)
	return

def play(mus):
	n = int(0)
	for i in len(mus):
		winsound.Beep(mus[n][0], mus[n][1])
		n += 1
	return

def emot_():
	fr = str(input())
	frec = int(r_int.randint(37, 32000))
	note = list()
	for i in fr:
		if len(fr) > 45:
			print("La maquina se agoto...")
			print("Reinicia para recargarla")
			return
		else:
			fr.split(" ")
			for i in fr:
				for e in i:
					if e.isupper() ==True:
						frec += random
					elif e.islower() ==True:
						frec -= random
					elif e.isnum() == True:
						frec = frec/(frec-(1/random))
					elif e.isalnum() == False:
						frec = random/(random-(1/frec))
					else:
						frec = random
					if frec < 37:
						frec = 37
					elif frec > 32000:
						frec = 32000
				dur = len(random)/(len(random)-(len(random/frec)))
				note.append(fr)
				note.append(dur)
			mus.append(note)
		print("Reproduciendo...")
		play(mus)
		return mus

def quo(c_c):
	print ("Musica:")
	print (c_c)
	print("Ta wena la musica?")
	b = bool(True)
	while b == True:
		answ = str(input)
		yes = ["1", "true", "si"]
		no = ["0", "false", "no"]
		if b.lower() in yes:
			cacheapp(c_c)
		elif b.lower() in no:
			b = False
			return
		else:
			pass
			
#winsound.Beep(frequency, duration) Beep the PC’s speaker. The frequency parameter specifies frequency, in hertz, of the sound, and must be in the range 37 through 32,767. The duration parameter specifies the number of milliseconds the sound should last. If the system is not able to beep the speaker, RuntimeError is raised.

print("###################################")
print("MUSICALIZADOR 0.01")
while True:
	c_c = emot_()
	quo(c_c)	
print("###################################")