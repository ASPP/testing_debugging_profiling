##### Mock basic
m = Mock()
m.x = 3
m.x
m.f(1,2,3)
m.whatever(3, key=2)
m
m.f
m.g

##### special attributes and assert methods
mock=Mock()
mock.f(2,3)
mock.f('a')

mock.f.called
mock.add.called
mock.f.called
mock.f.call_args
mock.f.call_count
mock.f.call_args_list
mock.f.assert_called_with('a')
mock.f.assert_called_once_with('a')
mock.f.assert_called_with(2, 3)
mock.f.assert_any_call(2, 3)
mock.f.assert_has_calls(['a', (2,3)])

#### return_value and side_effect
mock.g.return_value = 7
mock.g(32)
mock.g('r')

# useful to simulate file errors or server errors
mock.g.side_effect = Exception('Noooo')  
mock.g(2)
mock.g.side_effect = lambda x: x.append(2)
a=[1]
mock.g(a)
a

mock.g.side_effect = [1, 4, 5]
mock.g()
mock.g()
mock.g()
mock.g()

#####
mock = Mock()
mock.f(3,4)
mock.g('a')
mock.f.a()
mock.method_calls

result = m.h(32)
result(1)
m.mock_calls

##### spec
from chaco.api import Plot
m2 = Mock(spec=Plot)
isinstance(m2, Plot)
m2.add
m2.add(12,'asdfasd')
m2.aaa
