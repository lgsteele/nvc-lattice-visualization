from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt



primitive = .25*np.array([1,1,1])
bravais = .5*np.array([[1,1,0],[1,0,1],[0,1,1]])
##print bravais.shape
##print bravais*np.ones((4,1,1))



i = .5*np.array([1,1,0])
j = .5*np.array([1,0,1])
k = .5*np.array([0,1,1])

fcc1 = np.array([[0,0,0],\
                 i,j,k,\
                 i+j,i+k,j+k,\
                 2*i,2*j,2*k,\
                 i+j+k,i-j+k,i+j-k,-i+j+k])
fcc2 = fcc1+primitive

fcc11 = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,0],\
                  [1,1,0],[1,0,0],[0,1,0]])
fcc12 = fcc11+np.array([0,0,1])
fcc13 = np.array([[0,0,0],[0,1,0],[0,1,1],[0,0,1],[0,0,0],\
                  [0,1,1],[0,0,1],[0,1,0]])
fcc14 = fcc13+np.array([1,0,0])
fcc15 = np.array([[0,0,0],[1,0,0],[1,0,1],[0,0,1],[0,0,0],\
                 [1,0,1],[0,0,1],[1,0,0]])
fcc16 = fcc15+np.array([0,1,0])
fcc17 = np.array([[.5,.5,0],[.5,0,.5],[0,.5,.5],\
                  [.5,.5,1],[.5,1,.5],[1,.5,.5]])

fcc21 = fcc11+primitive
fcc22 = fcc12+primitive
fcc23 = fcc13+primitive
fcc24 = fcc14+primitive
fcc25 = fcc15+primitive
fcc26 = fcc16+primitive
fcc27 = fcc17+primitive

fcc30 = np.array([[.25,.25,.25],[.75,.75,.25],[.75,.25,.75],[.25,.75,.75]])
fcc31 = np.array([[0,0,0],[.25,.25,.25],[.5,.5,0],[.75,.75,.25],[1,1,0]])
fcc32 = np.array([[.5,0,.5],[.25,.25,.25],[0,.5,.5]])
fcc33 = np.array([[1,0,1],[.75,.25,.75],[.5,.5,1],[.25,.75,.75],[0,1,1]])
fcc34 = fcc32+np.array([.5,.5,0])
fcc35 = np.array([[.5,0,.5],[.75,.25,.75],[1,.5,.5]])
fcc36 = fcc35+np.array([-.5,.5,0])

##fcc1 = np.vstack((fcc11,fcc12,fcc13,fcc14))
fcc1 = fcc15

print fcc11.shape

fig = plt.figure(figsize=plt.figaspect(1.))
ax = fig.add_subplot(221, projection='3d')
ax.plot(fcc11[:,0],fcc11[:,1],fcc11[:,2],':k')
ax.plot(fcc12[:,0],fcc12[:,1],fcc12[:,2],'k')
ax.plot(fcc13[:,0],fcc13[:,1],fcc13[:,2],':k')
ax.plot(fcc14[:,0],fcc14[:,1],fcc14[:,2],'k')
ax.plot(fcc15[:,0],fcc15[:,1],fcc15[:,2],'k')
ax.plot(fcc16[:,0],fcc16[:,1],fcc16[:,2],':k')
ax.plot(fcc11[:,0],fcc11[:,1],fcc11[:,2],'ok',ms=10)
ax.plot(fcc12[:,0],fcc12[:,1],fcc12[:,2],'ok',ms=10)
ax.plot(fcc13[:,0],fcc13[:,1],fcc13[:,2],'ok',ms=10)
ax.plot(fcc14[:,0],fcc14[:,1],fcc14[:,2],'ok',ms=10)
ax.plot(fcc15[:,0],fcc15[:,1],fcc15[:,2],'ok',ms=10)
ax.plot(fcc16[:,0],fcc16[:,1],fcc16[:,2],'ok',ms=10)
ax.plot(fcc17[:,0],fcc17[:,1],fcc17[:,2],'ok',ms=10)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

ax = fig.add_subplot(222, projection='3d')
ax.plot(fcc11[:,0],fcc11[:,1],fcc11[:,2],':k')
ax.plot(fcc12[:,0],fcc12[:,1],fcc12[:,2],'k')
ax.plot(fcc13[:,0],fcc13[:,1],fcc13[:,2],':k')
ax.plot(fcc14[:,0],fcc14[:,1],fcc14[:,2],'k')
ax.plot(fcc15[:,0],fcc15[:,1],fcc15[:,2],'k')
ax.plot(fcc16[:,0],fcc16[:,1],fcc16[:,2],':k')
ax.plot(fcc11[:,0],fcc11[:,1],fcc11[:,2],'ok',ms=10)
ax.plot(fcc12[:,0],fcc12[:,1],fcc12[:,2],'ok',ms=10)
ax.plot(fcc13[:,0],fcc13[:,1],fcc13[:,2],'ok',ms=10)
ax.plot(fcc14[:,0],fcc14[:,1],fcc14[:,2],'ok',ms=10)
ax.plot(fcc15[:,0],fcc15[:,1],fcc15[:,2],'ok',ms=10)
ax.plot(fcc16[:,0],fcc16[:,1],fcc16[:,2],'ok',ms=10)
ax.plot(fcc17[:,0],fcc17[:,1],fcc17[:,2],'ok',ms=10)

ax.plot(fcc21[:,0],fcc21[:,1],fcc21[:,2],':g')
ax.plot(fcc22[:,0],fcc22[:,1],fcc22[:,2],'g')
ax.plot(fcc23[:,0],fcc23[:,1],fcc23[:,2],':g')
ax.plot(fcc24[:,0],fcc24[:,1],fcc24[:,2],'g')
ax.plot(fcc25[:,0],fcc25[:,1],fcc25[:,2],'g')
ax.plot(fcc26[:,0],fcc26[:,1],fcc26[:,2],':g')
ax.plot(fcc21[:,0],fcc21[:,1],fcc21[:,2],'og',ms=10)
ax.plot(fcc22[:,0],fcc22[:,1],fcc22[:,2],'og',ms=10)
ax.plot(fcc23[:,0],fcc23[:,1],fcc23[:,2],'og',ms=10)
ax.plot(fcc24[:,0],fcc24[:,1],fcc24[:,2],'og',ms=10)
ax.plot(fcc25[:,0],fcc25[:,1],fcc25[:,2],'og',ms=10)
ax.plot(fcc26[:,0],fcc26[:,1],fcc26[:,2],'og',ms=10)
ax.plot(fcc27[:,0],fcc27[:,1],fcc27[:,2],'og',ms=10)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

ax = fig.add_subplot(223, projection='3d')
ax.plot(fcc11[:,0],fcc11[:,1],fcc11[:,2],'ok',ms=10)
ax.plot(fcc12[:,0],fcc12[:,1],fcc12[:,2],'ok',ms=10)
ax.plot(fcc13[:,0],fcc13[:,1],fcc13[:,2],'ok',ms=10)
ax.plot(fcc14[:,0],fcc14[:,1],fcc14[:,2],'ok',ms=10)
ax.plot(fcc15[:,0],fcc15[:,1],fcc15[:,2],'ok',ms=10)
ax.plot(fcc16[:,0],fcc16[:,1],fcc16[:,2],'ok',ms=10)
ax.plot(fcc17[:,0],fcc17[:,1],fcc17[:,2],'ok',ms=10)
ax.plot(fcc30[:,0],fcc30[:,1],fcc30[:,2],'ok',ms=10)
ax.plot(fcc31[:,0],fcc31[:,1],fcc31[:,2],'b')
ax.plot(fcc32[:,0],fcc32[:,1],fcc32[:,2],'b')
ax.plot(fcc33[:,0],fcc33[:,1],fcc33[:,2],'b')
ax.plot(fcc34[:,0],fcc34[:,1],fcc34[:,2],'b')
ax.plot(fcc35[:,0],fcc35[:,1],fcc35[:,2],'b')
ax.plot(fcc36[:,0],fcc36[:,1],fcc36[:,2],'b')
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])


# NV Orientations
nvn1 = np.array([[1,0,1]])
nvn2 = np.array([[.5,.5,1]])
nvn3 = np.array([[1,.5,.5]])
nvn4 = np.array([[.5,0,.5]])
nvv = np.array([[.75,.25,.75]])
ax = fig.add_subplot(224, projection='3d')
ax.plot(fcc11[:,0],fcc11[:,1],fcc11[:,2],'ok',ms=10)
ax.plot(fcc12[:,0],fcc12[:,1],fcc12[:,2],'ok',ms=10)
ax.plot(fcc13[:,0],fcc13[:,1],fcc13[:,2],'ok',ms=10)
ax.plot(fcc14[:,0],fcc14[:,1],fcc14[:,2],'ok',ms=10)
ax.plot(fcc15[:,0],fcc15[:,1],fcc15[:,2],'ok',ms=10)
ax.plot(fcc16[:,0],fcc16[:,1],fcc16[:,2],'ok',ms=10)
ax.plot(fcc17[:,0],fcc17[:,1],fcc17[:,2],'ok',ms=10)
ax.plot(fcc30[:,0],fcc30[:,1],fcc30[:,2],'ok',ms=10)
ax.plot(nvn1[:,0],nvn1[:,1],nvn1[:,2],'og',ms=15)
ax.plot(nvn2[:,0],nvn2[:,1],nvn2[:,2],'og',ms=15)
ax.plot(nvn3[:,0],nvn3[:,1],nvn3[:,2],'og',ms=15)
ax.plot(nvn4[:,0],nvn4[:,1],nvn4[:,2],'og',ms=15)
ax.plot(nvv[:,0],nvv[:,1],nvv[:,2],'or',ms=15)

ax.plot(fcc31[:,0],fcc31[:,1],fcc31[:,2],':b')
ax.plot(fcc32[:,0],fcc32[:,1],fcc32[:,2],':b')
ax.plot(fcc33[:,0],fcc33[:,1],fcc33[:,2],':b')
ax.plot(fcc34[:,0],fcc34[:,1],fcc34[:,2],':b')
ax.plot(fcc35[:,0],fcc35[:,1],fcc35[:,2],':b')
ax.plot(fcc36[:,0],fcc36[:,1],fcc36[:,2],':b')
# Draw NVC axis lines
nvnv1 = np.vstack((nvn1,nvv))
nvnv2 = np.vstack((nvn2,nvv))
nvnv3 = np.vstack((nvn3,nvv))
nvnv4 = np.vstack((nvn4,nvv))
ax.plot(nvnv1[:,0],nvnv1[:,1],nvnv1[:,2],'k')
ax.plot(nvnv2[:,0],nvnv2[:,1],nvnv2[:,2],'k')
ax.plot(nvnv3[:,0],nvnv3[:,1],nvnv3[:,2],'k')
ax.plot(nvnv4[:,0],nvnv4[:,1],nvnv4[:,2],'k')
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

plt.show()

















