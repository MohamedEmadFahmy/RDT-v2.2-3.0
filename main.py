from network import NetworkLayer
from receiver import ReceiverProcess, RDTReceiver
from sender import SenderProcess, RDTSender
# import sys

if __name__ == "__main__":
    # args = dict([arg.split('=', maxsplit=1) for arg in sys.argv[1:]])
    # print(args)
    # msg = args['msg']
    # prob_to_deliver = float(args['rel'])
    # delay = int(args['delay'])
    # debug = bool(int(args['debug']))
    # corrupt_pkt = True
    # corrupt_ack = True
    # if debug:
    #     corrupt_pkt = bool(int(args["pkt"]))
    #     corrupt_ack = bool(int(args["ack"]))

    msg = "hi"
    prob_to_deliver = 1
    delay = 0
    corrupt_pkt = True
    corrupt_ack = True

    SenderProcess.set_outgoing_data(msg)

    # print(f"Sender is sending: {SenderProcess.get_outgoing_data()}")

    network_serv = NetworkLayer(
        reliability=prob_to_deliver,
        delay=delay,
        pkt_corrupt=corrupt_pkt,
        ack_corrupt=corrupt_ack,
    )

    rdt_sender = RDTSender(network_serv)
    rdt_sender.rdt_send(SenderProcess.get_outgoing_data())

    print(f"Receiver received: {ReceiverProcess.get_buffer()}")


# receiver = RDTReceiver()

# # Test Case 1: Valid Packet
# packet1 = {"sequence_number": "0", "data": "A", "checksum": 65}
# result1 = receiver.is_corrupted(packet1)
# print(f"Test Case 1: {packet1} -> Expected: False, Actual: {result1}")

# # Test Case 2: Corrupted Packet (Altered Data)
# packet2 = {"sequence_number": "0", "data": "B", "checksum": 65}
# result2 = receiver.is_corrupted(packet2)
# print(f"Test Case 2: {packet2} -> Expected: True, Actual: {result2}")

# # Test Case 3: Corrupted Packet (Altered Checksum)
# packet3 = {"sequence_number": "0", "data": "A", "checksum": 66}
# result3 = receiver.is_corrupted(packet3)
# print(f"Test Case 3: {packet3} -> Expected: True, Actual: {result3}")

# # Test Case 4: Valid Packet (Special Characters)
# packet4 = {"sequence_number": "1", "data": "#", "checksum": 35}
# result4 = receiver.is_corrupted(packet4)
# print(f"Test Case 4: {packet4} -> Expected: False, Actual: {result4}")

# # Test Case 5: Corrupted Packet (Mismatched Sequence Number)
# packet5 = {"sequence_number": "0", "data": "A", "checksum": 65}
# result5 = receiver.is_corrupted(packet5)
# print(f"Test Case 5: {packet5} -> Expected: True, Actual: {result5}")

# # Test Case 6: Corrupted Packet (Mismatched Sequence Number)
# packet6 = {"sequence_number": "1", "data": "A", "checksum": 65}
# result6 = receiver.is_corrupted(packet6)
# print(f"Test Case 6: {packet6} -> Expected: True, Actual: {result6}")
