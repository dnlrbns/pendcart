# pend cart

## Equations of motion

$$\ddot{x} = \frac{-\frac{1}{2}ml\cos(\theta)\ddot{\theta} - b\dot{x}+\frac{1}{2}ml\sin(\theta)\dot{\theta}^2}{M+m}$$

$$\ddot{\theta} = \frac{-\frac{1}{2}ml\cos(\theta)\ddot{x} - c\dot{x}+\frac{1}{2}ml\sin(\theta)\dot{x}\dot{\theta}}{\frac{m}{12}(3l+l^2)}$$

Combining:

$$\ddot{x} = \frac{-\frac{1}{2}ml\cos(\theta)\frac{-\frac{1}{2}ml\cos(\theta)\ddot{x} - c\dot{x}+\frac{1}{2}ml\sin(\theta)\dot{x}\dot{\theta}}{\frac{m}{12}(3l+l^2)} - b\dot{x}+\frac{1}{2}ml\sin(\theta)\dot{\theta}^2}{M+m}$$

$$\ddot{x} = \frac{\frac{\frac{1}{4}m^2l^2\cos^2(\theta)\ddot{x} +\frac{1}{2}ml\cos(\theta) c\dot{x}-\frac{1}{4}m^2l^2\sin(\theta)\cos(\theta)\dot{x}\dot{\theta}}{\frac{m}{12}(3l+l^2)} - b\dot{x}+\frac{1}{2}ml\sin(\theta)\dot{\theta}^2}{(M+m)}$$

$$\ddot{x} = \frac{\frac{\frac{1}{4}m^2l^2\cos^2(\theta)\ddot{x} +\frac{1}{2}ml\cos(\theta) c\dot{x}-\frac{1}{4}m^2l^2\sin(\theta)\cos(\theta)\dot{x}\dot{\theta}- b\dot{x}\frac{m}{12}(3l+l^2)+\frac{1}{2}ml\sin(\theta)\dot{\theta}^2\frac{m}{12}(3l+l^2)}{\frac{m}{12}(3l+l^2)}}{(M+m)}$$

$$\ddot{x} = \frac{\frac{1}{4}m^2l^2\cos^2(\theta)\ddot{x} +\frac{1}{2}ml\cos(\theta) c\dot{x}-\frac{1}{4}m^2l^2\sin(\theta)\cos(\theta)\dot{x}\dot{\theta}- b\dot{x}\frac{m}{12}(3l+l^2)+\frac{1}{2}ml\sin(\theta)\dot{\theta}^2\frac{m}{12}(3l+l^2)}{(M+m)\frac{m}{12}(3l+l^2)}$$

$$\ddot{x} = \frac{\frac{1}{4}m^2l^2\cos^2(\theta)\ddot{x} }{(M+m)\frac{m}{12}(3l+l^2)} + \frac{\frac{1}{2}ml\cos(\theta) c\dot{x}-\frac{1}{4}m^2l^2\sin(\theta)\cos(\theta)\dot{x}\dot{\theta}- b\dot{x}\frac{m}{12}(3l+l^2)+\frac{1}{2}ml\sin(\theta)\dot{\theta}^2\frac{m}{12}(3l+l^2)}{(M+m)\frac{m}{12}(3l+l^2)}$$

$$\ddot{x} - \frac{\frac{1}{4}m^2l^2\cos^2(\theta)\ddot{x} }{(M+m)\frac{m}{12}(3l+l^2)} = \frac{\frac{1}{2}ml\cos(\theta) c\dot{x}-\frac{1}{4}m^2l^2\sin(\theta)\cos(\theta)\dot{x}\dot{\theta}- b\dot{x}\frac{m}{12}(3l+l^2)+\frac{1}{2}ml\sin(\theta)\dot{\theta}^2\frac{m}{12}(3l+l^2)}{(M+m)\frac{m}{12}(3l+l^2)}$$

$$\ddot{x}\left(1 - \frac{\frac{1}{4}m^2l^2\cos^2(\theta)}{(M+m)\frac{m}{12}(3l+l^2)}\right) = \frac{\frac{1}{2}ml\cos(\theta) c\dot{x}-\frac{1}{4}m^2l^2\sin(\theta)\cos(\theta)\dot{x}\dot{\theta}- b\dot{x}\frac{m}{12}(3l+l^2)+\frac{1}{2}ml\sin(\theta)\dot{\theta}^2\frac{m}{12}(3l+l^2)}{(M+m)\frac{m}{12}(3l+l^2)}$$

$$\ddot{x} = \frac{\frac{1}{2}ml\cos(\theta) c\dot{x}-\frac{1}{4}m^2l^2\sin(\theta)\cos(\theta)\dot{x}\dot{\theta}- b\dot{x}\frac{m}{12}(3l+l^2)+\frac{1}{2}ml\sin(\theta)\dot{\theta}^2\frac{m}{12}(3l+l^2)}{(M+m)\frac{m}{12}(3l+l^2)\left(1 - \frac{\frac{1}{4}m^2l^2\cos^2(\theta)}{(M+m)\frac{m}{12}(3l+l^2)}\right)}$$