# video_converter

## Program

Il programma utilizza le librerie [`youtube-dl`](https://github.com/ytdl-org/youtube-dl) e [`FFmpeg`](https://github.com/FFmpeg) che possono essere usate separatamente oppure insieme.

* youtube-dl permette di scaricare i video dai siti presenti nella lista in mp4: [Supported Sites](https://ytdl-org.github.io/youtube-dl/supportedsites.html) 
* FFmpeg permette di convertire i video in formato mp3

A seconda di quello che si vuole fare bisogna modificare il file [`settings.json`](.\bin\settings.json)

Se un file è gia stato scaricato/convertito oppure ha lo stesso nome viene sostituito

## settings.json
Il file delle impostazioni funziona mettendo tra le virgolette una "T", le virgolette devono rimanere anche nel caso non si voglia attiva la determinata variabile, si può quindi lasciare vuota o mettere quealsiasi altro carattere es: "F"

	{
		"file_input_link": ".\\link.txt",		#la path del file con la lista dei link

		"audio_quality": "192k",				#la qualità audio del video scaricato

		"download_video": "T",					#attiva la libreria "youtube-dl" e scarica i video presenti nel file di input
												(può rimanere attiva senza problemi se il file dei link è vuoto)

		"remove_str_file": "T",					#se disattivato il nome dei file avrà alla fine del nome parte del link
												(funziona indipendentemente dalla variabile precedente)
												(consigliabile tenerla sempre attiva in assenza di relativi bug)

		"reset_file_input": "",					#resetta il file contenente i link a fine esecuzione
												(funziona indipendentemente dalle variabili precedenti)

		"convert_video": "",					#attiva la libreria "ffmpeg" convertendo i file appena scaricati
		"convert_existing_video": "",			#converte (anche) i video presenti nella cartella destinata ai video
												(funziona dipendentemente dalla variabile precedente)
												(può essere usata per convertire un file video in mp3)
		"delete_converted_video": "",			#elimina i video convertiti
												(funziona dipendentemente dalla variabile "convert_video")

		"dir_video": ".\\video",				#cartella predefinita per il download e processo di conversione dei video
												(conversione dei video esistenti prima dell'esecuzione del programma)
		"dir_audio": ".\\audio",				#cartella predefinita per la destinazione dei video convertiti

		
		"e_dir_video": ".\\e_video",			#cartella temporanea per il download dei video
		"e_dir_audio": ".\\e_audio",			#cartella temporanea per la conversione degli audio

												(le cartelle temporanee sono state create per evitare bug ad un eventuale secondo avvio del programma)

		"before": " ",							#sostituzione nel nome temporanea
		"after": "y_-s_-z"						#rinominazione temporanea (modificare se si presenta questa dicitura nel nome del video)
	}

## Installation
Per l'installazione si procede con il comando da terminale per youtube-dl: `pip install youtube-dl`.
Successivamente per la libreria FFmpeg, dopo aver scaricato la libreria da questo [link](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z), oppure eseguendo il file [ffmpeg_dl.bat](\ffmpeg_dl.bat), estraetela e rinominatela ffmpeg. Ora bisogna (come amministratori) andare su `Pannello di controllo>Sistema e sicurezza>Sistema` > `Impostazioni di sistema avanzate` > `Variabili d'ambiente`, premere su `Path` e fare `Modifica...`. Ora fate `Nuovo` ed incollate la path della cartella ffmpeg fino alla cartella bin (la cartella può essere messa dove si vuole, l'importante è che se si vuole spostare la cartella si modifichi anche la variabile d'ambiente)

Il risulatato dovrà essere simile a questo:

	C:\*\ffmpeg\bin

Per verificare l'installazione eseguire da linea comando:

	ffmpeg -version

## Requirements

python3, ffmpeg, youtube-dl

## Library

ffmpeg, youtube-dl

## Author

Vicentini Tommaso