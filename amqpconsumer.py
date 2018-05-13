#!/usr/bin/python

import configparser
import pika
from com.kkartikeya.home.weather.weather_pb2 import Weather
from com.kkartikeya.home.internet.speed_pb2 import Speed
from socket import socket, AF_INET, SOCK_DGRAM

CONFIG_FILE_PATH='/Users/kk/work/personal/github.com/configuration/config.properties'

def getAMQPURL():
	config=configparser.RawConfigParser()
	config.read(CONFIG_FILE_PATH)

	return config.get('Messaging', 'CLOUDAMQP_URL')

def consumeAMQPMessages( queue ):
    AMQPURL=getAMQPURL()
    params = pika.URLParameters(AMQPURL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel

    channel.queue_declare(queue)

    def callback(ch, method, properties, body):
        currentWeather=Weather()
        currentWeather.ParseFromString(body)
        print(" [x] Received %s" % currentWeather)

    channel.basic_consume(callback,
                          queue,
                          no_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()


def main():
    queue='weather'
    consumeAMQPMessages(queue)

if __name__ == "__main__":
    main()
