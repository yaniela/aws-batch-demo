import sys
import boto3
import json

def sumar_y_guardar(numero1, numero2, bucket, key):
    resultado = numero1 + numero2
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=key, Body=json.dumps({"resultado": resultado}))

if __name__ == "__main__":
    # Los argumentos se pasan como números 1, número 2, bucket S3, key S3
    #n1 = int(sys.argv[1])
    #n2 = int(sys.argv[2])    
    #bucket = sys.argv[3]
    #key = sys.argv[4]

    clientes_dict = {
    1: {2, 3},
    2: {3, 4, 5},
    3: {6}
    }
    
    bucket = 'aws-batch-testing-results'
    key = 'result-2-3.json'

    for n1, variables in clientes_dict.items():
        print(f"Cliente {n1} tiene las siguientes variables:")
        # Iterar sobre cada variable asociada a este cliente
        for n2 in variables:
            print(f"    Variable {n2}")  
            key = f'result-{n1}-{n2}.json'   
            sumar_y_guardar(n1, n2, bucket, key)
