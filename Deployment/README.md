
### Docker deploy
Ejecutar  'docker-compose up'. 

## Servicios

### etl

Corre el etl para generar 4 archivos csv que serán consumidos por games_api

### games_api

 Api con 4 servicios ir a  : http://localhost:8080/docs 

 - http://localhost:8080/game_service/get_top_10_games_console_company
 - http://localhost:8080/game_service/top_10_games_consoles
 - http://localhost:8080/game_service/worst_10_games_console_company
 - http://localhost:8080/game_service/worst_10_games_consoles
