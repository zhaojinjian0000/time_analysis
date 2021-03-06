set  name=20210305-zjj


set csvdir=./csvs/
set dir=./pics/
set ext=.csv
set suffix1=-efficience_pie_chart.png
set suffix2=-energy_trend.png
set suffix3=-time_matrix_pie_chart.png
python time_process_day.py -i %csvdir%%name%%ext% -o %dir%
python generate_wallpaper.py --chartpng  %dir%%name%%suffix1%   %dir%%name%%suffix2%   %dir%%name%%suffix3%
python change_wallpaper.py
pause