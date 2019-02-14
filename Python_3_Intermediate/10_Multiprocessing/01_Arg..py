import multiprocessing

def spawn(num):
	print('spawned! {}'.format( num ) )

#its neccessary in multiprocessing
#only run when the scripted one runned
#if the script called somethings else it will not run
if __name__ == '__main__':
	for i in range(5):
		p = multiprocessing.Process(target=spawn, args=( i, )) # allow to spawn a process , a target will be the function
		#arguament passing
		p.start()
		#p.join() #waiting for the process to be complete
		#if it is commeneted out, the proccess dont wait each others, runs parallel