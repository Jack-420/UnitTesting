import pytest, sys, os, json
from tut1.myapp.sample import add, valid_age, sub, mul, div, save_dict, Student

@pytest.mark.normal
class TestNormally:
    def test_add_num(self):
        assert add(2,3)==5
    
@pytest.mark.error
class TestErrors:
    def test_valid_age_valid(self):
        valid_age(10)
        
    def test_valid_age_invalid(self):
        with pytest.raises(ValueError, match="Age cannot be less than 0"):
            valid_age(-1) 

@pytest.mark.marker
class TestMarkers:
    @pytest.mark.skip(reason="Error hoga")
    def test_sub(self):
        assert sub(10,3)==7
        
    @pytest.mark.skipif(sys.version_info > (3,7),reason="Version is greater")
    def test_mul(self):
        assert mul(2,5)==10

    @pytest.mark.xfail(sys.platform=="linux",reason="The platform is not suitable")
    def test_div(self):
        assert div(2,0)==5
        
    @pytest.mark.parametrize("a,b,c",[(1,2,3),("ab","bc","abbc"),([1],[2,3],[1,2,3])], ids=["num","str","list"])
    def test_add(self,a,b,c):
        assert add(a,b)==c
        
@pytest.mark.ficture
class TestFicture: 
    def test_save_dict(self,tmpdir,capsys):
        filepath=os.path.join(tmpdir,"test.json")
        _dict={"a":1,"b":2}
        save_dict(_dict,filepath)
        assert json.load(open(filepath,'r'))==_dict
        assert capsys.readouterr().out=="saved\n"

@pytest.fixture(scope="class")
def dummy_student():
    return Student("Mrinal",22,10)

@pytest.mark.customFixture
class TestCustomFixture:
    
    def test_student_get_age(self,dummy_student):
        assert dummy_student.get_age()==22
        
    def test_student_get_credit(self,dummy_student):
        assert dummy_student.get_credit()==10
        
    def test_student_set_credit(self,dummy_student):
        dummy_student.set_credit(20)
        assert dummy_student.get_credit()==20
        
    
        

