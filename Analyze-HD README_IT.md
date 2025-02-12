
# Analyze-HD

Analyze-HD è uno script Python progettato per analizzare un'unità (drive) del computer e generare un report contenente l'elenco dei file più grandi di 1 GB. Questo può essere utile per identificare file che occupano spazio significativo nel disco.

## Funzionalità

- Esclude cartelle di sistema come `Windows`, `Program Files`, `$Recycle.Bin` per evitare di analizzare file non rilevanti.
- Cerca ricorsivamente file di grandi dimensioni in tutte le directory del drive specificato.
- Genera un report (`LargeFilesReport.txt`) contenente l'elenco dei file che superano 1 GB, con il percorso completo e la dimensione.

## Requisiti di sistema

- Python 3.6 o superiore
- Permessi di lettura sul drive specificato

## Dipendenze

Questo script utilizza solo librerie standard di Python, quindi non sono necessarie dipendenze aggiuntive.

## Come utilizzare

1. **Clona il repository**:
   ```bash
   git clone https://github.com/Tranchillo/Analyze-HD.git
   cd Analyze-HD
   ```

2. **Esegui lo script**:
   - Modifica la variabile `drive_to_analyze` nel file `analyze_hd.py` per specificare l'unità da analizzare (esempio: `C:\`).
   - Avvia lo script:
     ```bash
     python analyze_hd.py
     ```

3. **Output**:
   - Troverai il report generato nella directory radice del drive analizzato con il nome `LargeFilesReport.txt`.

## Note

- Lo script ignora errori di accesso ai file (ad esempio, permessi insufficienti).
- La dimensione dei file viene calcolata in base a una soglia predefinita di 1 GB. È possibile modificare questo valore modificando la variabile `size_limit` nello script.

## Licenza

Questo progetto è distribuito sotto la licenza GPL-3.0. Per maggiori dettagli, consulta il file LICENSE.
