import tensorflow as tf
import numpy as np

class GraphDrawer(object):
    """description of class"""

    sess = None
    x = None
    y = None
    mediumFitness = None
    summary_op = None
    writer = None
    i = 0

    def __init__(self, xAxisName, yAxisName):
        self.sess = tf.Session()
        self.x = tf.placeholder('float',name=xAxisName)
        self.y = tf.placeholder('float',name=yAxisName)
        self.mediumFitness = tf.add(self.x,self.y, name='add')
        tf.summary.scalar('Medium fitness', self.mediumFitness)
        self.summary_op = tf.summary.merge_all()
        self.sess.run(tf.global_variables_initializer())
        self.writer = tf.summary.FileWriter('Graphs',self.sess.graph)


    def addPoint(self,xAxisCoord,yAxisCoord):
        add, s_ = self.sess.run([self.mediumFitness, self.summary_op], feed_dict={self.x:xAxisCoord,self.y:yAxisCoord - self.i - 1})
        self.writer.add_summary(s_, self.i)
        self.i += 1

    #def writeGraph():
    #    x = tf.placeholder('float',name='Generation')
    #    y = tf.placeholder('float',name='Fitness')
    #    addition = tf.add(x,y, name='add')
    #    tf.summary.scalar('addition', addition)
    #    summary_op = tf.summary.merge_all()     
    #    with tf.Session() as sess:
    #        sess.run(tf.global_variables_initializer())
    #        writer = tf.summary.FileWriter('Graphs',sess.graph)
    #        for i in range(100):
    #            var1=  np.random.rand()
    #            var2=  np.random.rand()
    #            print(var1,var2)
    #            add, s_ = sess.run([addition, summary_op], feed_dict={x:var1,y:var2})
    #            writer.add_summary(s_, i)


