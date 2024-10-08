from network import NetworkLayer
from receiver import ReceiverProcess
from sender import SenderProcess, RDTSender
from colorama import Fore
import sys

if __name__ == "__main__":
    args = dict([arg.split('=', maxsplit = 1) for arg in sys.argv[1:]])
    print(args)
    msg = args['msg']
    prob_to_deliver = float(args['rel'])
    delay = int(args['delay'])
    debug = bool(int(args['debug']))
    corrupt_pkt = True
    corrupt_ack = True
    pkt_loss = True
    if debug:
        corrupt_pkt = bool(int(args["pkt"]))
        corrupt_ack = bool(int(args["ack"]))
        pkt_loss = bool(int(args["loss"]))

    # msg = "moski"
    # prob_to_deliver = 0.3
    # delay = 0
    # corrupt_pkt = True
    # corrupt_ack = True
    # pkt_loss = True

    SenderProcess.set_outgoing_data(msg)

    print(Fore.CYAN + "Welcome")
    print(Fore.CYAN + "-------")

    print(Fore.YELLOW + "Sender is sending: " + Fore.WHITE + SenderProcess.get_outgoing_data())
    print()

    network_serv = NetworkLayer(
        reliability=prob_to_deliver,
        delay=delay,
        pkt_corrupt=corrupt_pkt,
        ack_corrupt=corrupt_ack,
        pkt_loss = pkt_loss
    )

    rdt_sender = RDTSender(network_serv)
    rdt_sender.rdt_send(SenderProcess.get_outgoing_data())

    print()
    print()
    print(Fore.CYAN + "Final Message: " + Fore.WHITE + str(ReceiverProcess.get_buffer()))

