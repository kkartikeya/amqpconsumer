#!/usr/bin/python

import configparser
import pika
import threading
from com.kkartikeya.home.weather.weather_pb2 import Weather
from com.kkartikeya.home.internet.speed_pb2 import Speed
from statsdclient import StatsdClient

CONFIG_FILE_PATH='/Users/kk/work/personal/github.com/configuration/config.properties'

def getAMQPURL():
	config=configparser.RawConfigParser()
	config.read(CONFIG_FILE_PATH)

	return config.get('Messaging', 'CLOUDAMQP_URL')

def consumeAMQPMessages( queue ):
	if queue == 'weather':
		consumeWeatherAMQPMessages( queue )
	elif queue == 'internet':
		consumeBandwidthAMQPMessages( queue )

def consumeWeatherAMQPMessages( queue ):
    AMQPURL=getAMQPURL()
    params = pika.URLParameters(AMQPURL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel

    channel.queue_declare(queue)

    def callback(ch, method, properties, body):
        currentWeather=Weather()
        currentWeather.ParseFromString(body)
        print(" [x] Received Weather Data: %s" % currentWeather)
		StatsdClient.send({'com.kkartikeya.home.weather.temp':"%s|g" % currentWeather.temp }, ("127.0.0.1", 8125))
		StatsdClient.send({'com.kkartikeya.home.weather.humidity':"%s|g" % currentWeather.humidity }, ("127.0.0.1", 8125))
		StatsdClient.send({'com.kkartikeya.home.weather.windspeed':"%s|g" % currentWeather.windspeed }, ("127.0.0.1", 8125))
		StatsdClient.send({'com.kkartikeya.home.weather.cloud':"%s|g" % currentWeather.cloud }, ("127.0.0.1", 8125))

    channel.basic_consume(callback,
                          queue,
                          no_ack=True)

    print(' [*] Waiting for Weather messages:')
    channel.start_consuming()

def consumeBandwidthAMQPMessages( queue ):
    AMQPURL=getAMQPURL()
    params = pika.URLParameters(AMQPURL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel

    channel.queue_declare(queue)

    def callback(ch, method, properties, body):
        bandwidth=Speed()
        bandwidth.ParseFromString(body)
        print(" [x] Received Internet Bandwidth %s" % bandwidth)
		StatsdClient.send({'com.kkartikeya.home.internet.speed.download':"%s|g" % bandwidth.download }, ("127.0.0.1", 8125))
		StatsdClient.send({'com.kkartikeya.home.internet.speed.upload':"%s|g" % bandwidth.upload }, ("127.0.0.1", 8125))
		StatsdClient.send({'com.kkartikeya.home.internet.speed.ping':"%s|g" % bandwidth.ping }, ("127.0.0.1", 8125))

    channel.basic_consume(callback,
                          queue,
                          no_ack=True)

    print(' [*] Waiting for Bandwidth messages:')
    channel.start_consuming()

def main():
	queue = ('weather', 'internet')
	threads = []
	for i in range(len(queue)):
		t = threading.Thread(name=queue[i], target=consumeAMQPMessages, args=(queue[i],))
		threads.append(t)
		t.start()


if __name__ == "__main__":
    main()
