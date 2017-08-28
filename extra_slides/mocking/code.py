
>>> from smtplib import SMTP
>>> mock_smtp = Mock(spec=SMTP)

>>> isinstance(mock_smtp, SMTP)
True

>>> mock_smtp.<TAB>
                    mock_smtp.assert_any_call         mock_smtp.attach_mock             mock_smtp.call_args                
                    mock_smtp.assert_called_once_with mock_smtp.auth                    mock_smtp.call_args_list           
                    mock_smtp.assert_called_with      mock_smtp.auth_cram_md5           mock_smtp.call_count              >
                    mock_smtp.assert_has_calls        mock_smtp.auth_login              mock_smtp.called                   
                    mock_smtp.assert_not_called       mock_smtp.auth_plain              mock_smtp.close                    

>>> mock_smtp.bogus
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-17-4856e93b6e10> in <module>()
----> 1 mock_smtp.bogus

/Users/pberkes/miniconda3/envs/gnode/lib/python3.5/unittest/mock.py in __getattr__(self, name)
    576         elif self._mock_methods is not None:
    577             if name not in self._mock_methods or name in _all_magics:
--> 578                 raise AttributeError("Mock object has no attribute %r" % name)
    579         elif _is_magic(name):
    580             raise AttributeError(name)

AttributeError: Mock object has no attribute 'bogus'


