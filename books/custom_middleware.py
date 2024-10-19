import time

class TiempoDeProcesamientoMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self, request):
    # Codigo que se ejecuta antes de que la vista sea llamada
        tiempo_inicio = time.time()
        
        response = self.get_response(request)
        
    # Codigo que se ejecuta despues de que la vista ha sido llamada
        tiempo_fin = time.time()
        tiempo_total = tiempo_fin - tiempo_inicio
        
    # Añadir el tiempo de procesamiento a la respuesta como una cabezera HTTP
        response ["X-Tiempo-De-Procesamiento"] = str(tiempo_total)
        print(response["X-Tiempo-De-Procesamiento"])
        return response
    