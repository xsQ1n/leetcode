# python总结

## time库

### time.strftime()

#### 描述

Python time strftime() 函数用于格式化时间，返回以可读字符串表示的当地时间，格式由参数 format 决定。

#### 语法

strftime()方法语法：

```
time.strftime(format[, t])
```

#### 参数

- format -- 格式字符串。
- t -- 可选的参数 t 是一个 struct_time 对象。

#### 返回值

返回以可读字符串表示的当地时间。

#### 使用

```
time.strftime("%Y%m%d_%H%M%S",time.localtime())
```

