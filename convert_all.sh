#!/bin/bash
FFMPEG="/c/Users/valen/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1-full_build/bin/ffmpeg.exe"
OUT="/c/Users/valen/Documents/PROYECTOS/PORTAFOLIO/VIDEOS_MP4"
LOG="/c/Users/valen/Documents/PROYECTOS/PORTAFOLIO/conversion_log.txt"

echo "=== INICIO CONVERSION $(date) ===" > "$LOG"

convert() {
  local url="$1"
  local outdir="$2"
  local outname="$3"
  local has_audio="$4"
  
  echo "[$(date +%H:%M:%S)] Descargando $outname..." >> "$LOG"
  curl -L -s -o "$OUT/$outdir/$outname.mov" "$url"
  
  if [ "$has_audio" = "yes" ]; then
    "$FFMPEG" -i "$OUT/$outdir/$outname.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "$OUT/$outdir/$outname.mp4" -y 2>/dev/null
  else
    "$FFMPEG" -i "$OUT/$outdir/$outname.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -an "$OUT/$outdir/$outname.mp4" -y 2>/dev/null
  fi
  
  if [ -f "$OUT/$outdir/$outname.mp4" ]; then
    local orig=$(stat -c%s "$OUT/$outdir/$outname.mov" 2>/dev/null || stat -f%z "$OUT/$outdir/$outname.mov")
    local new=$(stat -c%s "$OUT/$outdir/$outname.mp4" 2>/dev/null || stat -f%z "$OUT/$outdir/$outname.mp4")
    echo "[$(date +%H:%M:%S)] OK: $outname.mp4 ($orig -> $new bytes)" >> "$LOG"
    rm "$OUT/$outdir/$outname.mov"
  else
    echo "[$(date +%H:%M:%S)] ERROR: $outname falló" >> "$LOG"
  fi
}

# HOME-IMPROVEMENT (5 videos, muted = no audio)
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/1.mov" "HOME-IMPROVEMENT" "1" "no"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/2.mov" "HOME-IMPROVEMENT" "2" "no"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/3.mov" "HOME-IMPROVEMENT" "3" "no"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/3.3.mov" "HOME-IMPROVEMENT" "3.3" "no"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/1.4.mov" "HOME-IMPROVEMENT" "1.4" "no"

# ENERGIA-FITNESS (8 videos, con audio)
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/videos/MODALIDAD.mov" "ENERGIA-FITNESS/videos" "MODALIDAD" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/videos/PROMOCION.mov" "ENERGIA-FITNESS/videos" "PROMOCION" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/VIDEO%20PRESENTACION.mov" "ENERGIA-FITNESS" "VIDEO-PRESENTACION" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/videos/energia-fitness.mov" "ENERGIA-FITNESS/videos" "energia-fitness" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-2.mov" "ENERGIA-FITNESS/semana-hype" "semana-hype-2" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-3.mov" "ENERGIA-FITNESS/semana-hype" "semana-hype-3" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-4.mov" "ENERGIA-FITNESS/semana-hype" "semana-hype-4" "yes"

# NATAN-BARBER (6 videos)
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/natan%20ahora.mov" "NATAN-BARBER" "natan-ahora" "no"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/0307.mov" "NATAN-BARBER/videos" "0307" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/asmr.mov" "NATAN-BARBER/videos" "asmr" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/corte-primer-plano.mov" "NATAN-BARBER/videos" "corte-primer-plano" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/session-1.mov" "NATAN-BARBER/videos" "session-1" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/session-2.mov" "NATAN-BARBER/videos" "session-2" "yes"

# AGENCY-LUXURY (15 videos + 2 VSLs)
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/1%C2%B0RIA%C3%91O29.10.2025%20CON%20PORTADA.mov" "AGENCY-LUXURY/videos" "1-RIANIO-CON-PORTADA" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/AGENCY%20LUXURY.mov" "AGENCY-LUXURY/videos" "AGENCY-LUXURY" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20-%20CAIDA%20DE%20MAMAS.mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY-CAIDA-DE-MAMAS" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(1).mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY-1" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(2).mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY-2" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(3).mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY-3" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(4).mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY-4" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(5).mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY-5" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(6).mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY-6" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(7).mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY-7" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(8).mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY-8" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(9).mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY-9" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY.mov" "AGENCY-LUXURY/videos" "LUXURY-AGENCY" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/luxury-agency.mov" "AGENCY-LUXURY/videos" "luxury-agency" "yes"
convert "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/PIN%20PONG-LUXURY%20AGENCY.mov" "AGENCY-LUXURY/videos" "PIN-PONG-LUXURY-AGENCY" "yes"
convert "https://valentin-cdn.b-cdn.net/VSL%20RIGE%C3%91O.mov" "VSL" "VSL-RIGENIO" "yes"
convert "https://valentin-cdn.b-cdn.net/VSL%20REDISE%C3%91O%20DE%20MAMAS.mov" "VSL" "VSL-REDISENO-DE-MAMAS" "yes"

echo "=== FIN CONVERSION $(date) ===" >> "$LOG"
echo "TODOS LOS VIDEOS CONVERTIDOS" >> "$LOG"
