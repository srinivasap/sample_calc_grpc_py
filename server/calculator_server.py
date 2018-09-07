from concurrent import futures
import time
import grpc

#import sys
#sys.path.insert(0, '/Users/z001hmr/MSSE/Fall2018/CMPE273\ Ent\ Dist\ Systems/genereated')

import calculator_pb2
import calculator_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculator(calculator_pb2_grpc.CalculatorServicer):

    def AddNumbers(self, request, context):
        return calculator_pb2.AddReponse(result = request.num1 + request.num2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()