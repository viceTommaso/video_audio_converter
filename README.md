﻿# video_audio_converter


## Prerequisites
windows, [python 3](https://www.python.org/downloads/)

## Library
[FFmpeg](https://github.com/FFmpeg/FFmpeg), [youtube-dl](https://github.com/ytdl-org/youtube-dl)

## Installation
Per l'installazione si procede con il comando da terminale per youtube-dl: `pip install youtube-dl` oppure eseguendo il file [setup.bat](\etc\setup.bat).

Successivamente per la libreria FFmpeg, dopo aver scaricato la libreria da questo [link](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z), oppure eseguendo il file [ffmpeg_dl.bat](\etc\ffmpeg_dl.bat), estraetela e rinominatela ffmpeg. Ora bisogna (come amministratori) andare su `Pannello di controllo>Sistema e sicurezza>Sistema` > `Impostazioni di sistema avanzate` > `Variabili d'ambiente`, premere su `Path` e fare `Modifica...`. Ora fate `Nuovo` ed incollate la path della cartella ffmpeg fino alla cartella bin (la cartella può essere messa dove si vuole, l'importante è che se si vuole spostare la cartella si modifichi anche la variabile d'ambiente)

Il risulatato dovrà essere simile a questo:

	C:\*\ffmpeg\bin

Per verificare l'installazione eseguire da linea comando:

	ffmpeg -version

## Program
Il programma può essere utilizzato per scaricare i video (anche playlist) da diversi siti e/o convertire i video in audio, più nello specifico: utilizza le librerie [`youtube-dl`](https://github.com/ytdl-org/youtube-dl) e [`FFmpeg`](https://github.com/FFmpeg/FFmpeg) che possono essere usate separatamente oppure insieme.

* youtube-dl permette di scaricare i video dai siti presenti nella lista in mp4: [Supported Sites](https://ytdl-org.github.io/youtube-dl/supportedsites.html) 
* FFmpeg permette di convertire i video in formato mp3

A seconda di quello che si vuole fare bisogna modificare il file [`settings.json`](.\bin\settings.json)

Se si vuole scaricare uno o più video contemporaneamente, basta mettere i link nell'apposito file ([`link.txt`](.\bin\link.txt) o quello che scieglierete) inserendo i link uno sotto l'altro

Altrimenti si può eseguire il programma da prompt dei comandi come ultimo parametro il link del video (eseguendolo in questo modo il file con i link non verrà resettato anche se la variabile è attiva)

Se un file è gia stato scaricato/convertito oppure ha lo stesso nome viene ignorato

***SI CONSIGLIA DI ESEGUIRE IL PROGRAMMA A VUOTO PRIMA DELL'USO***

P.S. Nomi di file troppo lunghi o con molti spazi potrebbero esserci errori. È risolvibile modificando nel programma ciò che viene sostituito al carattere " " nella funzione error_char (riga 44). Sempre nella stessa funzione possono essere aggiunti altri caratteri che possono dare errore.

## settings.json
Il file delle impostazioni funziona mettendo tra le virgolette una "T", le virgolette devono rimanere anche nel caso non si voglia attiva la determinata variabile, si può quindi lasciare vuota o mettere qualsiasi altro carattere es: "F"
Nei percorsi dei file si raccomanda il doppio backslash in modo da non dare problemi nell'esecuzione

	{
		"file_input_link": ".\\link.txt",		#la path del file con la lista dei link

		"audio_quality": "192k",			#la qualità audio del video scaricato

		"download_video": "T",				#attiva la libreria "youtube-dl" e scarica i video presenti nel file di input (risoluzione massima 720p)
								(può rimanere attiva senza problemi se il file dei link è vuoto)

		"remove_str_file": "T",				#se disattivato il nome dei file avrà alla fine del nome parte del link
								Se eseguendo questa operazione i file risultano con lo stesso nome, al secondo file verra aggiunto " - COPY"
								(funziona indipendentemente dalla variabile precedente)
								(consigliabile tenerla sempre attiva in assenza di relativi bug)

		"reset_file_input": "",				#resetta il file contenente i link a fine esecuzione
								(funziona indipendentemente dalle variabili precedenti)

		"convert_video": "",				#attiva la libreria "ffmpeg" convertendo i file appena scaricati
		"convert_existing_video": "",			#converte (anche) i video presenti nella cartella destinata ai video
								(funziona dipendentemente dalla variabile precedente)
								(può essere usata per convertire un file video in mp3)
		"delete_converted_video": "",			#elimina i video convertiti. Se attiva questa variabile il download sarà più rapido perche invece di scaricare video e audio a massima qualità, sarà solo l'audio ad essere migliore
								(funziona dipendentemente dalla variabile "convert_video")

		"dir_video": ".\\video",			#cartella predefinita per il download e processo di conversione dei video
								(conversione dei video esistenti prima dell'esecuzione del programma)
		"dir_audio": ".\\audio",			#cartella predefinita per la destinazione dei video convertiti

		
		"e_dir_video": ".\\e_video",			#cartella temporanea per il download dei video
								(questa cartella sarà nascosta se generata automaticamente)
		"e_dir_audio": ".\\e_audio",			#cartella temporanea per la conversione degli audio
								(questa cartella sarà nascosta se generata automaticamente)

								(le cartelle temporanee sono state create per evitare bug ad un eventuale secondo avvio del programma)
	}

## Problems
Se si riscontrano problemi con la libreria youtube-dl probabilmente bisogna aggiornarla con il comando: `pip install --upgrade youtube_dl` oppure eseguendo il file [setup.bat](\etc\setup.bat).

Se il problema deriva dalla libreria FFmpeg può esserci qualche carattere che crea errori, dunque aggiungere all'interno del programma il carattere che deve essere sostituito

## Author
Vicentini Tommaso
