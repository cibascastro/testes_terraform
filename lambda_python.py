import psycopg2
import schedule
import time

def call_procedure():
    try:
        # Conexão com o banco
        conn = psycopg2.connect(
            dbname="nome_do_banco",
            user="usuario",
            password="senha",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        
        # Chamada da procedure
        cursor.execute("CALL nome_da_procedure();")
        conn.commit()

        print("Procedure chamada com sucesso.")
    except Exception as e:
        print(f"Erro ao chamar procedure: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Agendamento a cada 30 segundos
schedule.every(30).seconds.do(call_procedure)

print("Iniciando o agendamento...")
while True:
    schedule.run_pending()
    time.sleep(1)
