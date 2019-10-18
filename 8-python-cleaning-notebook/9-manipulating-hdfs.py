# import pandas as pd
# from hdfs import InsecureClient
#
# #Cebd1160/Cebd1160!
# # emr update dfs.namenode.http-address
# hadoop conf
# client_hdfs = InsecureClient('http://ec2-34-204-70-68.compute-1.amazonaws.com:50070', 'hadoop')
#
# # Listing all files in HDFS
# fnames = client_hdfs.list('/')
# print(fnames)
#
# client_hdfs.makedirs('/test')
#
# # with client_hdfs.write('/test/sample-file.txt') as writer:
# #     writer.write('adding one line to a file called sample-file.txt')
#
# # Creating a simple Pandas DataFrame
# liste_hello = ['hello1', 'hello2']
# liste_world = ['world1', 'world2']
# df = pd.DataFrame(data={'hello': liste_hello, 'world': liste_world})
#
# # Writing Dataframe to hdfs
# with client_hdfs.write('/test/helloworld.csv', encoding='utf-8') as writer:
#   df.to_csv(writer)
# # #
# # # ====== Reading files ======
# # with client_hdfs.read('/test/helloworld.csv', encoding='utf-8') as reader:
# #   df = pd.read_csv(reader, index_col=0)
# #
