@echo off
setlocal enabledelayedexpansion
set FFMPEG="C:\Users\valen\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\ffmpeg.exe"
set OUT="C:\Users\valen\Documents\PROYECTOS\PORTAFOLIO\VIDEOS_MP4"

echo ============================================
echo   CONVERSION .MOV a .MP4 - Portfolio Valentin
echo   38 videos totales
echo ============================================
echo.

REM ===== HOME-IMPROVEMENT (5 videos) =====
echo [1/38] HOME-IMPROVEMENT/1.mov
curl -L -o "%OUT%\HOME-IMPROVEMENT\1.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/1.mov"
%FFMPEG% -i "%OUT%\HOME-IMPROVEMENT\1.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -an "%OUT%\HOME-IMPROVEMENT\1.mp4" -y
del "%OUT%\HOME-IMPROVEMENT\1.mov"
echo.

echo [2/38] HOME-IMPROVEMENT/2.mov
curl -L -o "%OUT%\HOME-IMPROVEMENT\2.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/2.mov"
%FFMPEG% -i "%OUT%\HOME-IMPROVEMENT\2.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -an "%OUT%\HOME-IMPROVEMENT\2.mp4" -y
del "%OUT%\HOME-IMPROVEMENT\2.mov"
echo.

echo [3/38] HOME-IMPROVEMENT/3.3.mov
curl -L -o "%OUT%\HOME-IMPROVEMENT\3.3.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/3.3.mov"
%FFMPEG% -i "%OUT%\HOME-IMPROVEMENT\3.3.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -an "%OUT%\HOME-IMPROVEMENT\3.3.mp4" -y
del "%OUT%\HOME-IMPROVEMENT\3.3.mov"
echo.

echo [4/38] HOME-IMPROVEMENT/1.4.mov
curl -L -o "%OUT%\HOME-IMPROVEMENT\1.4.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/1.4.mov"
%FFMPEG% -i "%OUT%\HOME-IMPROVEMENT\1.4.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -an "%OUT%\HOME-IMPROVEMENT\1.4.mp4" -y
del "%OUT%\HOME-IMPROVEMENT\1.4.mov"
echo.

echo [5/38] HOME-IMPROVEMENT/3.mov (referenciado en home.html)
curl -L -o "%OUT%\HOME-IMPROVEMENT\3.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/3.mov"
%FFMPEG% -i "%OUT%\HOME-IMPROVEMENT\3.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -an "%OUT%\HOME-IMPROVEMENT\3.mp4" -y
del "%OUT%\HOME-IMPROVEMENT\3.mov"
echo.

REM ===== ENERGIA-FITNESS (9 videos) =====
echo [6/38] ENERGIA-FITNESS/videos/MODALIDAD.mov
curl -L -o "%OUT%\ENERGIA-FITNESS\videos\MODALIDAD.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/videos/MODALIDAD.mov"
%FFMPEG% -i "%OUT%\ENERGIA-FITNESS\videos\MODALIDAD.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\ENERGIA-FITNESS\videos\MODALIDAD.mp4" -y
del "%OUT%\ENERGIA-FITNESS\videos\MODALIDAD.mov"
echo.

echo [7/38] ENERGIA-FITNESS/videos/PROMOCION.mov
curl -L -o "%OUT%\ENERGIA-FITNESS\videos\PROMOCION.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/videos/PROMOCION.mov"
%FFMPEG% -i "%OUT%\ENERGIA-FITNESS\videos\PROMOCION.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\ENERGIA-FITNESS\videos\PROMOCION.mp4" -y
del "%OUT%\ENERGIA-FITNESS\videos\PROMOCION.mov"
echo.

echo [8/38] ENERGIA-FITNESS/VIDEO PRESENTACION.mov
curl -L -o "%OUT%\ENERGIA-FITNESS\VIDEO-PRESENTACION.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/VIDEO%%20PRESENTACION.mov"
%FFMPEG% -i "%OUT%\ENERGIA-FITNESS\VIDEO-PRESENTACION.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\ENERGIA-FITNESS\VIDEO-PRESENTACION.mp4" -y
del "%OUT%\ENERGIA-FITNESS\VIDEO-PRESENTACION.mov"
echo.

echo [9/38] ENERGIA-FITNESS/videos/energia-fitness.mov
curl -L -o "%OUT%\ENERGIA-FITNESS\videos\energia-fitness.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/videos/energia-fitness.mov"
%FFMPEG% -i "%OUT%\ENERGIA-FITNESS\videos\energia-fitness.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\ENERGIA-FITNESS\videos\energia-fitness.mp4" -y
del "%OUT%\ENERGIA-FITNESS\videos\energia-fitness.mov"
echo.

echo [10/38] ENERGIA-FITNESS/semana-hype/semana-hype-1.mov
curl -L -o "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-1.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-1.mov"
%FFMPEG% -i "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-1.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-1.mp4" -y
del "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-1.mov"
echo.

echo [11/38] ENERGIA-FITNESS/semana-hype/semana-hype-2.mov
curl -L -o "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-2.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-2.mov"
%FFMPEG% -i "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-2.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-2.mp4" -y
del "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-2.mov"
echo.

echo [12/38] ENERGIA-FITNESS/semana-hype/semana-hype-3.mov
curl -L -o "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-3.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-3.mov"
%FFMPEG% -i "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-3.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-3.mp4" -y
del "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-3.mov"
echo.

echo [13/38] ENERGIA-FITNESS/semana-hype/semana-hype-4.mov
curl -L -o "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-4.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-4.mov"
%FFMPEG% -i "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-4.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-4.mp4" -y
del "%OUT%\ENERGIA-FITNESS\semana-hype\semana-hype-4.mov"
echo.

REM ===== NATAN-BARBER (6 videos) =====
echo [14/38] NATAN-BARBER/natan ahora.mov
curl -L -o "%OUT%\NATAN-BARBER\natan-ahora.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/natan%%20ahora.mov"
%FFMPEG% -i "%OUT%\NATAN-BARBER\natan-ahora.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -an "%OUT%\NATAN-BARBER\natan-ahora.mp4" -y
del "%OUT%\NATAN-BARBER\natan-ahora.mov"
echo.

echo [15/38] NATAN-BARBER/videos/0307.mov
curl -L -o "%OUT%\NATAN-BARBER\videos\0307.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/0307.mov"
%FFMPEG% -i "%OUT%\NATAN-BARBER\videos\0307.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\NATAN-BARBER\videos\0307.mp4" -y
del "%OUT%\NATAN-BARBER\videos\0307.mov"
echo.

echo [16/38] NATAN-BARBER/videos/asmr.mov
curl -L -o "%OUT%\NATAN-BARBER\videos\asmr.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/asmr.mov"
%FFMPEG% -i "%OUT%\NATAN-BARBER\videos\asmr.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\NATAN-BARBER\videos\asmr.mp4" -y
del "%OUT%\NATAN-BARBER\videos\asmr.mov"
echo.

echo [17/38] NATAN-BARBER/videos/corte-primer-plano.mov
curl -L -o "%OUT%\NATAN-BARBER\videos\corte-primer-plano.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/corte-primer-plano.mov"
%FFMPEG% -i "%OUT%\NATAN-BARBER\videos\corte-primer-plano.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\NATAN-BARBER\videos\corte-primer-plano.mp4" -y
del "%OUT%\NATAN-BARBER\videos\corte-primer-plano.mov"
echo.

echo [18/38] NATAN-BARBER/videos/session-1.mov
curl -L -o "%OUT%\NATAN-BARBER\videos\session-1.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/session-1.mov"
%FFMPEG% -i "%OUT%\NATAN-BARBER\videos\session-1.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\NATAN-BARBER\videos\session-1.mp4" -y
del "%OUT%\NATAN-BARBER\videos\session-1.mov"
echo.

echo [19/38] NATAN-BARBER/videos/session-2.mov
curl -L -o "%OUT%\NATAN-BARBER\videos\session-2.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/session-2.mov"
%FFMPEG% -i "%OUT%\NATAN-BARBER\videos\session-2.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\NATAN-BARBER\videos\session-2.mp4" -y
del "%OUT%\NATAN-BARBER\videos\session-2.mov"
echo.

REM ===== AGENCY-LUXURY (17 videos) =====
echo [20/38] AGENCY-LUXURY/videos/1 RIANIO 29.10.2025 CON PORTADA.mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\1-RIANIO-CON-PORTADA.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/1%%C2%%B0RIA%%C3%%91O29.10.2025%%20CON%%20PORTADA.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\1-RIANIO-CON-PORTADA.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\1-RIANIO-CON-PORTADA.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\1-RIANIO-CON-PORTADA.mov"
echo.

echo [21/38] AGENCY-LUXURY/videos/AGENCY LUXURY.mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\AGENCY-LUXURY.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/AGENCY%%20LUXURY.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\AGENCY-LUXURY.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\AGENCY-LUXURY.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\AGENCY-LUXURY.mov"
echo.

echo [22/38] AGENCY-LUXURY/videos/LUXURY AGENCY - CAIDA DE MAMAS.mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-CAIDA-DE-MAMAS.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY%%20-%%20CAIDA%%20DE%%20MAMAS.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-CAIDA-DE-MAMAS.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-CAIDA-DE-MAMAS.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-CAIDA-DE-MAMAS.mov"
echo.

echo [23/38] AGENCY-LUXURY/videos/LUXURY AGENCY (1).mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-1.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY%%20%%281%%29.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-1.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-1.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-1.mov"
echo.

echo [24/38] AGENCY-LUXURY/videos/LUXURY AGENCY (2).mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-2.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY%%20%%282%%29.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-2.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-2.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-2.mov"
echo.

echo [25/38] AGENCY-LUXURY/videos/LUXURY AGENCY (3).mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-3.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY%%20%%283%%29.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-3.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-3.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-3.mov"
echo.

echo [26/38] AGENCY-LUXURY/videos/LUXURY AGENCY (4).mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-4.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY%%20%%284%%29.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-4.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-4.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-4.mov"
echo.

echo [27/38] AGENCY-LUXURY/videos/LUXURY AGENCY (5).mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-5.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY%%20%%285%%29.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-5.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-5.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-5.mov"
echo.

echo [28/38] AGENCY-LUXURY/videos/LUXURY AGENCY (6).mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-6.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY%%20%%286%%29.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-6.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-6.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-6.mov"
echo.

echo [29/38] AGENCY-LUXURY/videos/LUXURY AGENCY (7).mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-7.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY%%20%%287%%29.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-7.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-7.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-7.mov"
echo.

echo [30/38] AGENCY-LUXURY/videos/LUXURY AGENCY (8).mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-8.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY%%20%%288%%29.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-8.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-8.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-8.mov"
echo.

echo [31/38] AGENCY-LUXURY/videos/LUXURY AGENCY (9).mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-9.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY%%20%%289%%29.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-9.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-9.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY-9.mov"
echo.

echo [32/38] AGENCY-LUXURY/videos/LUXURY AGENCY.mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%%20AGENCY.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\LUXURY-AGENCY.mov"
echo.

echo [33/38] AGENCY-LUXURY/videos/luxury-agency.mov (minusculas)
curl -L -o "%OUT%\AGENCY-LUXURY\videos\luxury-agency.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/luxury-agency.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\luxury-agency.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\luxury-agency.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\luxury-agency.mov"
echo.

echo [34/38] AGENCY-LUXURY/videos/PIN PONG-LUXURY AGENCY.mov
curl -L -o "%OUT%\AGENCY-LUXURY\videos\PIN-PONG-LUXURY-AGENCY.mov" "https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/PIN%%20PONG-LUXURY%%20AGENCY.mov"
%FFMPEG% -i "%OUT%\AGENCY-LUXURY\videos\PIN-PONG-LUXURY-AGENCY.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\AGENCY-LUXURY\videos\PIN-PONG-LUXURY-AGENCY.mp4" -y
del "%OUT%\AGENCY-LUXURY\videos\PIN-PONG-LUXURY-AGENCY.mov"
echo.

REM ===== VSLs (raiz del CDN) (2 videos) =====
echo [35/38] VSL RIGENIO.mov
curl -L -o "%OUT%\VSL\VSL-RIGENIO.mov" "https://valentin-cdn.b-cdn.net/VSL%%20RIGE%%C3%%91O.mov"
%FFMPEG% -i "%OUT%\VSL\VSL-RIGENIO.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\VSL\VSL-RIGENIO.mp4" -y
del "%OUT%\VSL\VSL-RIGENIO.mov"
echo.

echo [36/38] VSL REDISENO DE MAMAS.mov
curl -L -o "%OUT%\VSL\VSL-REDISENO-DE-MAMAS.mov" "https://valentin-cdn.b-cdn.net/VSL%%20REDISE%%C3%%91O%%20DE%%20MAMAS.mov"
%FFMPEG% -i "%OUT%\VSL\VSL-REDISENO-DE-MAMAS.mov" -c:v libx264 -crf 26 -preset slow -movflags +faststart -vf scale=1280:-2 -c:a aac -b:a 128k "%OUT%\VSL\VSL-REDISENO-DE-MAMAS.mp4" -y
del "%OUT%\VSL\VSL-REDISENO-DE-MAMAS.mov"
echo.

REM ===== kord3.html y manblue.html YA ESTAN EN .mp4 - NO necesitan conversion =====

echo.
echo ============================================
echo   CONVERSION COMPLETA! (36 videos)
echo   Los archivos .mp4 estan en:
echo   C:\Users\valen\Documents\PROYECTOS\PORTAFOLIO\VIDEOS_MP4\
echo.
echo   SIGUIENTE PASO: Subi estos .mp4 a Bunny CDN
echo   en las MISMAS carpetas donde estaban los .mov
echo ============================================
pause
