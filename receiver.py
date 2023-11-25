import colorama
from colorama import Fore
class ReceiverProcess:
    """Represent the receiver process in the application layer"""

    __buffer = list()

    @staticmethod
    def deliver_data(data):
        """deliver data from the transport layer RDT receiver to the application layer
        :param data: a character received by the RDT RDT receiver
        :return: no return value
        """
        ReceiverProcess.__buffer.append(data)
        return

    @staticmethod
    def get_buffer():
        """To get the message the process received over the network
        :return:  a python list of characters represent the incoming message
        """
        return ReceiverProcess.__buffer


class RDTReceiver:
    """ " Implement the Reliable Data Transfer Protocol V2.2 Receiver Side"""

    def __init__(self):
        self.sequence = "0"

    @staticmethod
    def is_corrupted(packet):
        """Check if the received packet from sender is corrupted or not
        :param packet: a python dictionary represent a packet received from the sender
        :return: True -> if the reply is corrupted | False ->  if the reply is NOT corrupted
        """
        # TODO provide your own implementation

        new_checksum = ord(packet["data"])
        return new_checksum != int(packet["checksum"])

    @staticmethod
    def is_expected_seq(rcv_pkt, exp_seq):
        """Check if the received reply from receiver has the expected sequence number
        :param rcv_pkt: a python dictionary represent a packet received by the receiver
        :param exp_seq: the receiver expected sequence number '0' or '1' represented as a character
        :return: True -> if ack in the reply match the   expected sequence number otherwise False
        """
        # TODO provide your own implementation

        # print(rcv_pkt)
        return rcv_pkt["sequence_number"] == exp_seq

    @staticmethod
    def make_reply_pkt(seq, checksum):
        """Create a reply (feedback) packet with to acknowledge the received packet
        :param seq: the sequence number '0' or '1' to be acknowledged
        :param checksum: the checksum of the ack the receiver will send to the sender
        :return:  a python dictionary represent a reply (acknowledgement)  packet
        """
        reply_pck = {"ack": seq, "checksum": checksum}
        return reply_pck

    def rdt_rcv(self, rcv_pkt):
        """Implement the RDT v2.2 for the receiver
        :param rcv_pkt: a packet delivered by the network layer 'udt_send()' to the receiver
        :return: the reply packet
        """

        # TODO provide your own implementation

        seq_to_send = self.sequence

        # print(Fore.RED + "Reciever: Expected sequence number: {}".format(self.sequence))
        # print()

        if self.is_corrupted(rcv_pkt) or not self.is_expected_seq(rcv_pkt, self.sequence):
            print(Fore.RED + "network_layer: \033[4mcorruption occured\033[0m" + str(rcv_pkt))
            print(Fore.GREEN + "Receiver \033[4mExpecting Sequence number:\033[0m" + Fore.WHITE + str(self.sequence))

            if seq_to_send == "0":
                seq_to_send = "1"
            else:
                seq_to_send = "0"
            
            reply_pkt = RDTReceiver.make_reply_pkt(seq_to_send, ord(seq_to_send))

            print(Fore.GREEN + "Receiver \033[4mReply packet:\033[0m" + Fore.WHITE + str(reply_pkt))

        else:

            reply_pkt = RDTReceiver.make_reply_pkt(seq_to_send, ord(seq_to_send))
            print(Fore.GREEN + "Receiver \033[4mExpecting Sequence number:\033[0m" + Fore.WHITE + str(self.sequence))
            print(Fore.GREEN + "Receiver \033[4mReply packet:\033[0m" + Fore.WHITE + str(reply_pkt))
            if self.sequence == "0":
                self.sequence = "1"
            else:
                self.sequence = "0"

            # deliver the data to the process in the application layer ONLY if the data is not corrupt
            ReceiverProcess.deliver_data(rcv_pkt["data"])


        return reply_pkt
