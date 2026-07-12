from queue import Queue

queue = Queue()

request_id = 1


def generate_request():
    global request_id

    queue.put(f"application #{request_id}")
    print(f"Created: application #y{request_id}")
    request_id += 1


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processed: {request}")
    else:
        print("Queue is empty")


#main loop
while True:
    generate_request()
    process_request()

    answer = input("Continue? (y/n): ")

    if answer.lower() == "n":
        break