import random


# Task text:
# In a digital information transmission system, speech is transmitted in digital form.
# Voice packets are transmitted through 2 transit channels, buffered in drives before each channel.
# The packet transmission time over the channel is 5 ms. Packets arrive in 6+-3 ms.
# Packets transmitted for more than 10 ms are destroyed at the system output,
# since their appearance in the decoder will significantly reduce the quality of the transmitted speech.
# Destroying more than 30% of packets is unacceptable. When this level is reached,
# the system uses resources to speed up transmission to 4 ms per channel.
# When the level drops to an acceptable level, resources are turned off.

# Objectives:
# Simulate 10 seconds of system operation.
# Determine the frequency of packet destruction and the frequency of resource connection.
def transfer_speech_in_digital_format():
    # 0 - time when packet arrived
    # 1 - time after packet pass first channel
    # 2 - time after packet pass second channel
    m = [0, 5, 10]
    l = [0, 0, 0]
    queue = [[0] * 100] * 4
    packet_timing_before_goes_to_decoder = [0] * 100

    total_packets_counter = 0
    packets_counter = 0
    packets_counter_with_resources = 0
    packets_destroyed_counter = 0

    time = 0
    time_limit = 10000
    while time < time_limit:
        # Find the minimum value in m
        i = 0
        time = m[0]
        for j in range(3):
            if m[j] < time:
                time = m[j]
                i = j

        if i == 0:
            total_packets_counter += 1

            l[0] += 1
            queue[1][l[0]] = m[0]

            l[2] += 1
            packet_timing_before_goes_to_decoder[l[2]] = m[0]

            r = random.uniform(0, 1)
            m[0] += 6 + 3 * (2 * r - 1)
        else:
            if (packets_counter != 0) or (packets_counter_with_resources != 0):
                result = (packets_destroyed_counter / (packets_counter + packets_counter_with_resources)) * 100
            else:
                result = 0

            if result <= 30:
                speed = 5
            else:
                speed = 4

            if i == 1:
                if l[0] != 0:
                    m[1] += speed
                    l[1] += 1
                    queue[2][l[1]] = m[1]

                    l[0] -= 1
                    for j in range(l[0]):
                        queue[1][j] = queue[1][j + 1]
                else:
                    m[1] = m[0]
            else:
                if l[1] != 0:
                    l[1] -= 1
                    for j in range(l[1]):
                        queue[2][j] = queue[2][j + 1]

                    m[2] += speed
                    if (m[2] - packet_timing_before_goes_to_decoder[1]) > 10:
                        packets_destroyed_counter += 1
                    else:
                        if speed == 5:
                            packets_counter += 1
                        else:
                            packets_counter_with_resources += 1

                    l[2] -= 1
                    for j in range(l[2]):
                        packet_timing_before_goes_to_decoder[j] = packet_timing_before_goes_to_decoder[j + 1]
                else:
                    m[2] = m[1]

    rcf = packets_counter_with_resources / (packets_counter + packets_counter_with_resources)
    pdf = packets_destroyed_counter / (packets_counter + packets_counter_with_resources)
    return time, total_packets_counter, packets_counter, packets_counter_with_resources, rcf, packets_destroyed_counter, pdf


if __name__ == "__main__":
    attempts = 5000
    results_size = 7
    results = [0] * results_size
    for attempt in range(attempts):
        result = transfer_speech_in_digital_format()

        for i in range(results_size):
            results[i] += result[i]

    for i in range(results_size):
        results[i] /= attempts

    print("System execution time..................", results[0])
    print("Packets transferred (total)............", results[1])
    print("Packets transferred without resources..", results[2])
    print("Packets transferred with resources.....", results[3])
    print("Resource connection frequency..........", results[4])
    print("Packets destroyed......................", results[5])
    print("Packets destroying frequency...........", results[6])
