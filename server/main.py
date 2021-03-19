import service_pb2 as service
import service_pb2_grpc as grpc_service
import grpc
import math
import os
from concurrent.futures import ThreadPoolExecutor


class Calculator(grpc_service.CalculatorServicer):
    def Solve(self, request, context):
        a = request.A
        b = request.B
        c = request.C

        d = b**2 - 4*a*c
        if d < 0:
            return service.EquationCalculatedMessage(realSolutionExists=False)
        elif d == 0:
            x1 = -b/(2 * a)
            x2 = -b/(2 * a)
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)

        return service.EquationCalculatedMessage(x1=x1, x2=x2, realSolutionExists=True)


server = grpc.server(ThreadPoolExecutor(max_workers=4))
grpc_service.add_CalculatorServicer_to_server(Calculator(), server)
host = os.environ.get('host') or '127.0.0.1'
port = os.environ.get('port') or 8008
print(f'Starting on {host}:{port}')
server.add_insecure_port(f'{host}:{port}')
server.start()

try:
    server.wait_for_termination()
except KeyboardInterrupt:
    print('\nShutting down')
